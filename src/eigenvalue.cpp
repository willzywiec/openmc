#include "openmc/eigenvalue.h"

#include "xtensor/xbuilder.hpp"
#include "xtensor/xmath.hpp"
#include "xtensor/xtensor.hpp"
#include "xtensor/xview.hpp"

#include "openmc/array.h"
#include "openmc/bank.h"
#include "openmc/capi.h"
#include "openmc/constants.h"
#include "openmc/error.h"
#include "openmc/hdf5_interface.h"
#include "openmc/ifp.h"
#include "openmc/math_functions.h"
#include "openmc/mesh.h"
#include "openmc/message_passing.h"
#include "openmc/output.h"
#include "openmc/random_lcg.h"
#include "openmc/search.h"
#include "openmc/settings.h"
#include "openmc/simulation.h"
#include "openmc/tallies/tally.h"
#include "openmc/timer.h"

#include <algorithm> // for min
#include <cmath>     // for sqrt, abs, pow
#include <iterator>  // for back_inserter
#include <limits>    //for infinity
#include <string>

#include <fmt/core.h>

namespace openmc {

//==============================================================================
// Global variables
//==============================================================================

namespace simulation {

double keff_generation;
array<double, 2> k_sum;
vector<double> entropy;
xt::xtensor<double, 1> source_frac;

// Delayed neutron kinetics parameters
double keff_prompt_generation {0.0};
vector<double> k_prompt;
double keff_prompt {0.0};
double keff_prompt_std {0.0};
double beta_eff {0.0};
double beta_eff_std {0.0};

// IFP-weighted alpha eigenvalue
// Computed from existing IFP scores: α = (k - 1) / Λ_eff
// where Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
double alpha_ifp {0.0};
double alpha_ifp_std {0.0};
double lambda_eff_ifp {0.0};
double lambda_eff_ifp_std {0.0};

// Index of internal kinetics tally (for alpha calculations using IFP)
int kinetics_tally_index {-1};

// Accumulators for k_prompt statistics (reset in openmc_finalize)
double k_prompt_sum {0.0};
double k_prompt_sum_sq {0.0};

} // namespace simulation

//==============================================================================
// Non-member functions
//==============================================================================

void calculate_generation_keff()
{
  const auto& gt = simulation::global_tallies;

  // Get keff for this generation by subtracting off the starting value
  simulation::keff_generation =
    gt(GlobalTally::K_TRACKLENGTH, TallyResult::VALUE) -
    simulation::keff_generation;

  double keff_reduced;
#ifdef OPENMC_MPI
  if (settings::solver_type != SolverType::RANDOM_RAY) {
    // Combine values across all processors
    MPI_Allreduce(&simulation::keff_generation, &keff_reduced, 1, MPI_DOUBLE,
      MPI_SUM, mpi::intracomm);
  } else {
    // If using random ray, MPI parallelism is provided by domain replication.
    // As such, all fluxes will be reduced at the end of each transport sweep,
    // such that all ranks have identical scalar flux vectors, and will all
    // independently compute the same value of k. Thus, there is no need to
    // perform any additional MPI reduction here.
    keff_reduced = simulation::keff_generation;
  }
#else
  keff_reduced = simulation::keff_generation;
#endif

  // Normalize single batch estimate of k
  // TODO: This should be normalized by total_weight, not by n_particles
  if (settings::solver_type != SolverType::RANDOM_RAY) {
    keff_reduced /= settings::n_particles;
  }

  simulation::k_generation.push_back(keff_reduced);
}

void calculate_generation_prompt_keff()
{
  // Only calculate if enabled
  if (!settings::calculate_prompt_k)
    return;

  // Get k_prompt for this generation by subtracting off the starting value
  simulation::keff_prompt_generation =
    global_tally_prompt_tracklength - simulation::keff_prompt_generation;

  double keff_prompt_reduced;
#ifdef OPENMC_MPI
  if (settings::solver_type != SolverType::RANDOM_RAY) {
    // Combine values across all processors
    MPI_Allreduce(&simulation::keff_prompt_generation, &keff_prompt_reduced, 1,
      MPI_DOUBLE, MPI_SUM, mpi::intracomm);
  } else {
    // For random ray, all ranks have identical flux and compute the same k
    keff_prompt_reduced = simulation::keff_prompt_generation;
  }
#else
  keff_prompt_reduced = simulation::keff_prompt_generation;
#endif

  // Normalize single batch estimate of k_prompt
  if (settings::solver_type != SolverType::RANDOM_RAY) {
    keff_prompt_reduced /= settings::n_particles;
  }

  simulation::k_prompt.push_back(keff_prompt_reduced);
}

void synchronize_bank()
{
  simulation::time_bank.start();

  // In order to properly understand the fission bank algorithm, you need to
  // think of the fission and source bank as being one global array divided
  // over multiple processors. At the start, each processor has a random amount
  // of fission bank sites -- each processor needs to know the total number of
  // sites in order to figure out the probability for selecting
  // sites. Furthermore, each proc also needs to know where in the 'global'
  // fission bank its own sites starts in order to ensure reproducibility by
  // skipping ahead to the proper seed.

#ifdef OPENMC_MPI
  int64_t start = 0;
  int64_t n_bank = simulation::fission_bank.size();
  MPI_Exscan(&n_bank, &start, 1, MPI_INT64_T, MPI_SUM, mpi::intracomm);

  // While we would expect the value of start on rank 0 to be 0, the MPI
  // standard says that the receive buffer on rank 0 is undefined and not
  // significant
  if (mpi::rank == 0)
    start = 0;

  int64_t finish = start + simulation::fission_bank.size();
  int64_t total = finish;
  MPI_Bcast(&total, 1, MPI_INT64_T, mpi::n_procs - 1, mpi::intracomm);

#else
  int64_t start = 0;
  int64_t finish = simulation::fission_bank.size();
  int64_t total = finish;
#endif

  // If there are not that many particles per generation, it's possible that no
  // fission sites were created at all on a single processor. Rather than add
  // extra logic to treat this circumstance, we really want to ensure the user
  // runs enough particles to avoid this in the first place.

  if (simulation::fission_bank.size() == 0) {
    fatal_error(
      "No fission sites banked on MPI rank " + std::to_string(mpi::rank));
  }

  simulation::time_bank_sample.start();

  // Allocate temporary source bank -- we don't really know how many fission
  // sites were created, so overallocate by a factor of 3
  int64_t index_temp = 0;

  vector<SourceSite> temp_sites(3 * simulation::work_per_rank);

  // Temporary banks for IFP
  vector<vector<int>> temp_delayed_groups;
  vector<vector<double>> temp_lifetimes;
  if (settings::ifp_on) {
    resize_ifp_data(
      temp_delayed_groups, temp_lifetimes, 3 * simulation::work_per_rank);
  }

  // ==========================================================================
  // SAMPLE N_PARTICLES FROM FISSION BANK AND PLACE IN TEMP_SITES

  // We use Uniform Combing method to exactly get the targeted particle size
  // [https://doi.org/10.1080/00295639.2022.2091906]

  // Make sure all processors use the same random number seed.
  int64_t id = simulation::total_gen + overall_generation();
  uint64_t seed = init_seed(id, STREAM_TRACKING);

  // Comb specification
  double teeth_distance = static_cast<double>(total) / settings::n_particles;
  double teeth_offset = prn(&seed) * teeth_distance;

  // First and last hitting tooth
  int64_t end = start + simulation::fission_bank.size();
  int64_t tooth_start = std::ceil((start - teeth_offset) / teeth_distance);
  int64_t tooth_end = std::floor((end - teeth_offset) / teeth_distance) + 1;

  // Locally comb particles in fission_bank
  double tooth = tooth_start * teeth_distance + teeth_offset;
  for (int64_t i = tooth_start; i < tooth_end; i++) {
    int64_t idx = std::floor(tooth) - start;
    temp_sites[index_temp] = simulation::fission_bank[idx];
    if (settings::ifp_on) {
      copy_ifp_data_from_fission_banks(
        idx, temp_delayed_groups[index_temp], temp_lifetimes[index_temp]);
    }
    ++index_temp;

    // Next tooth
    tooth += teeth_distance;
  }

  // At this point, the sampling of source sites is done and now we need to
  // figure out where to send source sites. Since it is possible that one
  // processor's share of the source bank spans more than just the immediate
  // neighboring processors, we have to perform an ALLGATHER to determine the
  // indices for all processors

#ifdef OPENMC_MPI
  // First do an exclusive scan to get the starting indices for
  start = 0;
  MPI_Exscan(&index_temp, &start, 1, MPI_INT64_T, MPI_SUM, mpi::intracomm);
  finish = start + index_temp;

  // TODO: protect for MPI_Exscan at rank 0

  // Allocate space for bank_position if this hasn't been done yet
  int64_t bank_position[mpi::n_procs];
  MPI_Allgather(
    &start, 1, MPI_INT64_T, bank_position, 1, MPI_INT64_T, mpi::intracomm);
#else
  start = 0;
  finish = index_temp;
#endif

  simulation::time_bank_sample.stop();
  simulation::time_bank_sendrecv.start();

#ifdef OPENMC_MPI
  // ==========================================================================
  // SEND BANK SITES TO NEIGHBORS

  // IFP number of generation
  int ifp_n_generation;
  if (settings::ifp_on) {
    broadcast_ifp_n_generation(
      ifp_n_generation, temp_delayed_groups, temp_lifetimes);
  }

  int64_t index_local = 0;
  vector<MPI_Request> requests;

  // IFP send buffers
  vector<int> send_delayed_groups;
  vector<double> send_lifetimes;

  if (start < settings::n_particles) {
    // Determine the index of the processor which has the first part of the
    // source_bank for the local processor
    int neighbor = upper_bound_index(
      simulation::work_index.begin(), simulation::work_index.end(), start);

    // Resize IFP send buffers
    if (settings::ifp_on && mpi::n_procs > 1) {
      resize_ifp_data(send_delayed_groups, send_lifetimes,
        ifp_n_generation * 3 * simulation::work_per_rank);
    }

    while (start < finish) {
      // Determine the number of sites to send
      int64_t n =
        std::min(simulation::work_index[neighbor + 1], finish) - start;

      // Initiate an asynchronous send of source sites to the neighboring
      // process
      if (neighbor != mpi::rank) {
        requests.emplace_back();
        MPI_Isend(&temp_sites[index_local], static_cast<int>(n),
          mpi::source_site, neighbor, mpi::rank, mpi::intracomm,
          &requests.back());

        if (settings::ifp_on) {
          // Send IFP data
          send_ifp_info(index_local, n, ifp_n_generation, neighbor, requests,
            temp_delayed_groups, send_delayed_groups, temp_lifetimes,
            send_lifetimes);
        }
      }

      // Increment all indices
      start += n;
      index_local += n;
      ++neighbor;

      // Check for sites out of bounds -- this only happens in the rare
      // circumstance that a processor close to the end has so many sites that
      // it would exceed the bank on the last processor
      if (neighbor > mpi::n_procs - 1)
        break;
    }
  }

  // ==========================================================================
  // RECEIVE BANK SITES FROM NEIGHBORS OR TEMPORARY BANK

  start = simulation::work_index[mpi::rank];
  index_local = 0;

  // IFP receive buffers
  vector<int> recv_delayed_groups;
  vector<double> recv_lifetimes;
  vector<DeserializationInfo> deserialization_info;

  // Determine what process has the source sites that will need to be stored at
  // the beginning of this processor's source bank.

  int neighbor;
  if (start >= bank_position[mpi::n_procs - 1]) {
    neighbor = mpi::n_procs - 1;
  } else {
    neighbor =
      upper_bound_index(bank_position, bank_position + mpi::n_procs, start);
  }

  // Resize IFP receive buffers
  if (settings::ifp_on && mpi::n_procs > 1) {
    resize_ifp_data(recv_delayed_groups, recv_lifetimes,
      ifp_n_generation * simulation::work_per_rank);
  }

  while (start < simulation::work_index[mpi::rank + 1]) {
    // Determine how many sites need to be received
    int64_t n;
    if (neighbor == mpi::n_procs - 1) {
      n = simulation::work_index[mpi::rank + 1] - start;
    } else {
      n = std::min(bank_position[neighbor + 1],
            simulation::work_index[mpi::rank + 1]) -
          start;
    }

    if (neighbor != mpi::rank) {
      // If the source sites are not on this processor, initiate an
      // asynchronous receive for the source sites

      requests.emplace_back();
      MPI_Irecv(&simulation::source_bank[index_local], static_cast<int>(n),
        mpi::source_site, neighbor, neighbor, mpi::intracomm, &requests.back());

      if (settings::ifp_on) {
        // Receive IFP data
        receive_ifp_data(index_local, n, ifp_n_generation, neighbor, requests,
          recv_delayed_groups, recv_lifetimes, deserialization_info);
      }

    } else {
      // If the source sites are on this processor, we can simply copy them
      // from the temp_sites bank

      index_temp = start - bank_position[mpi::rank];
      std::copy(&temp_sites[index_temp], &temp_sites[index_temp + n],
        &simulation::source_bank[index_local]);

      if (settings::ifp_on) {
        copy_partial_ifp_data_to_source_banks(
          index_temp, n, index_local, temp_delayed_groups, temp_lifetimes);
      }
    }

    // Increment all indices
    start += n;
    index_local += n;
    ++neighbor;
  }

  // Since we initiated a series of asynchronous ISENDs and IRECVs, now we have
  // to ensure that the data has actually been communicated before moving on to
  // the next generation

  int n_request = requests.size();
  MPI_Waitall(n_request, requests.data(), MPI_STATUSES_IGNORE);

  if (settings::ifp_on) {
    deserialize_ifp_info(ifp_n_generation, deserialization_info,
      recv_delayed_groups, recv_lifetimes);
  }

#else
  std::copy(temp_sites.data(), temp_sites.data() + settings::n_particles,
    simulation::source_bank.begin());
  if (settings::ifp_on) {
    copy_complete_ifp_data_to_source_banks(temp_delayed_groups, temp_lifetimes);
  }
#endif

  simulation::time_bank_sendrecv.stop();
  simulation::time_bank.stop();
}

void calculate_average_keff()
{
  // Determine overall generation and number of active generations
  int i = overall_generation() - 1;
  int n;
  if (simulation::current_batch > settings::n_inactive) {
    n = settings::gen_per_batch * simulation::n_realizations +
        simulation::current_gen;
  } else {
    n = 0;
  }

  if (n <= 0) {
    // For inactive generations, use current generation k as estimate for next
    // generation
    simulation::keff = simulation::k_generation[i];
  } else {
    // Sample mean of keff
    simulation::k_sum[0] += simulation::k_generation[i];
    simulation::k_sum[1] += std::pow(simulation::k_generation[i], 2);

    // Determine mean
    simulation::keff = simulation::k_sum[0] / n;

    if (n > 1) {
      double t_value;
      if (settings::confidence_intervals) {
        // Calculate t-value for confidence intervals
        double alpha = 1.0 - CONFIDENCE_LEVEL;
        t_value = t_percentile(1.0 - alpha / 2.0, n - 1);
      } else {
        t_value = 1.0;
      }

      // Standard deviation of the sample mean of k
      simulation::keff_std =
        t_value *
        std::sqrt(
          (simulation::k_sum[1] / n - std::pow(simulation::keff, 2)) / (n - 1));

      // In some cases (such as an infinite medium problem), random ray
      // may estimate k exactly and in an unvarying manner between iterations.
      // In this case, the floating point roundoff between the division and the
      // power operations may cause an extremely small negative value to occur
      // inside the sqrt operation, leading to NaN. If this occurs, we check for
      // it and set the std dev to zero.
      if (!std::isfinite(simulation::keff_std)) {
        simulation::keff_std = 0.0;
      }
    }
  }
}

void calculate_kinetics_parameters()
{
  // Only calculate if enabled
  if (!settings::calculate_prompt_k)
    return;

  // Determine overall generation and number of active generations
  int i = overall_generation() - 1;
  int n;
  if (simulation::current_batch > settings::n_inactive) {
    n = settings::gen_per_batch * simulation::n_realizations +
        simulation::current_gen;
  } else {
    n = 0;
  }

  if (n <= 0) {
    // For inactive generations, use current generation values as estimates
    simulation::keff_prompt = simulation::k_prompt[i];
  } else {
    // Accumulate sums for k_prompt (using namespace-level variables)
    simulation::k_prompt_sum += simulation::k_prompt[i];
    simulation::k_prompt_sum_sq += std::pow(simulation::k_prompt[i], 2);

    // Calculate mean k_prompt
    simulation::keff_prompt = simulation::k_prompt_sum / n;

    // Calculate standard deviation if we have enough samples
    if (n > 1) {
      double t_value;
      if (settings::confidence_intervals) {
        double alpha = 1.0 - CONFIDENCE_LEVEL;
        t_value = t_percentile(1.0 - alpha / 2.0, n - 1);
      } else {
        t_value = 1.0;
      }
      simulation::keff_prompt_std =
        t_value *
        std::sqrt((simulation::k_prompt_sum_sq / n - std::pow(simulation::keff_prompt, 2)) /
                  (n - 1));
    }

    // Calculate β_eff from k-prompt: β_eff = (k - k_prompt) / k
    if (simulation::keff > 0.0) {
      simulation::beta_eff =
        (simulation::keff - simulation::keff_prompt) / simulation::keff;

      if (n > 1) {
        double term1 = std::pow(1.0 / simulation::keff, 2) *
                       std::pow(simulation::keff_prompt_std, 2);
        double term2 =
          std::pow(simulation::keff_prompt / std::pow(simulation::keff, 2), 2) *
          std::pow(simulation::keff_std, 2);
        simulation::beta_eff_std = std::sqrt(term1 + term2);
      }
    }

    // Calculate IFP-weighted Λ_eff and α if enabled and tally exists
    // Uses IFP scores for generation time:
    //   Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
    //   α = (ρ - β_eff) / Λ_eff, where ρ = (k - 1) / k
    if (settings::calculate_alpha && simulation::kinetics_tally_index >= 0 &&
        settings::ifp_on) {
      auto& tally = *model::tallies[simulation::kinetics_tally_index];
      const auto& results = tally.results();

      int sum_idx = static_cast<int>(TallyResult::SUM);
      int sum_sq_idx = static_cast<int>(TallyResult::SUM_SQ);

      // IFP scores: index 0 = time-num, index 1 = denom
      double ifp_time_num = results(0, 0, sum_idx) / n;
      double ifp_denom = results(0, 1, sum_idx) / n;

      if (ifp_denom > 0.0 && simulation::keff > 0.0) {
        // Calculate Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
        simulation::lambda_eff_ifp = ifp_time_num / (ifp_denom * simulation::keff);

        // Calculate α = (ρ - β_eff) / Λ_eff, where ρ = (k - 1) / k
        // Physical interpretation:
        //   α < 0: subcritical (prompt neutrons decaying)
        //   α = 0: prompt critical
        //   α > 0: prompt supercritical (prompt neutrons growing)
        if (simulation::lambda_eff_ifp > 0.0) {
          double rho = (simulation::keff - 1.0) / simulation::keff;
          simulation::alpha_ifp =
            (rho - simulation::beta_eff) / simulation::lambda_eff_ifp;

          // Error propagation for Λ_eff and α
          if (n > 1) {
            auto calc_std = [&](int score_idx) {
              double mean = results(0, score_idx, sum_idx) / n;
              double sum_sq = results(0, score_idx, sum_sq_idx) / n;
              double variance = (sum_sq - mean * mean) / (n - 1);
              return (variance > 0.0) ? std::sqrt(variance) : 0.0;
            };

            double ifp_time_num_std = calc_std(0);
            double ifp_denom_std = calc_std(1);

            // Error propagation for Λ_eff = time_num / (denom × k)
            double dL_dnum = 1.0 / (ifp_denom * simulation::keff);
            double dL_ddenom = -ifp_time_num / (ifp_denom * ifp_denom * simulation::keff);
            double dL_dk = -ifp_time_num / (ifp_denom * simulation::keff * simulation::keff);

            double var_L = dL_dnum * dL_dnum * ifp_time_num_std * ifp_time_num_std +
                           dL_ddenom * dL_ddenom * ifp_denom_std * ifp_denom_std +
                           dL_dk * dL_dk * simulation::keff_std * simulation::keff_std;
            simulation::lambda_eff_ifp_std = std::sqrt(var_L);

            // Error propagation for α = (ρ - β) / Λ
            // ∂α/∂β = -1/Λ, ∂α/∂k = 1/(k²Λ) (via ∂ρ/∂k = 1/k²), ∂α/∂Λ = -(ρ-β)/Λ²
            double dAlpha_dBeta = -1.0 / simulation::lambda_eff_ifp;
            double dAlpha_dk = 1.0 / (simulation::keff * simulation::keff *
                                      simulation::lambda_eff_ifp);
            double dAlpha_dLambda =
              -(rho - simulation::beta_eff) /
              (simulation::lambda_eff_ifp * simulation::lambda_eff_ifp);

            double var_alpha_ifp =
              dAlpha_dBeta * dAlpha_dBeta * simulation::beta_eff_std * simulation::beta_eff_std +
              dAlpha_dk * dAlpha_dk * simulation::keff_std * simulation::keff_std +
              dAlpha_dLambda * dAlpha_dLambda * simulation::lambda_eff_ifp_std *
                simulation::lambda_eff_ifp_std;

            simulation::alpha_ifp_std = std::sqrt(var_alpha_ifp);
          }
        }
      }
    }
  }
}

int openmc_get_keff(double* k_combined)
{
  k_combined[0] = 0.0;
  k_combined[1] = 0.0;

  // Special case for n <=3. Notice that at the end,
  // there is a N-3 term in a denominator.
  if (simulation::n_realizations <= 3 ||
      settings::solver_type == SolverType::RANDOM_RAY) {
    k_combined[0] = simulation::keff;
    k_combined[1] = simulation::keff_std;
    if (simulation::n_realizations <= 1) {
      k_combined[1] = std::numeric_limits<double>::infinity();
    }
    return 0;
  }

  // Initialize variables
  int64_t n = simulation::n_realizations;

  // Copy estimates of k-effective and its variance (not variance of the mean)
  const auto& gt = simulation::global_tallies;

  array<double, 3> kv {};
  xt::xtensor<double, 2> cov = xt::zeros<double>({3, 3});
  kv[0] = gt(GlobalTally::K_COLLISION, TallyResult::SUM) / n;
  kv[1] = gt(GlobalTally::K_ABSORPTION, TallyResult::SUM) / n;
  kv[2] = gt(GlobalTally::K_TRACKLENGTH, TallyResult::SUM) / n;
  cov(0, 0) =
    (gt(GlobalTally::K_COLLISION, TallyResult::SUM_SQ) - n * kv[0] * kv[0]) /
    (n - 1);
  cov(1, 1) =
    (gt(GlobalTally::K_ABSORPTION, TallyResult::SUM_SQ) - n * kv[1] * kv[1]) /
    (n - 1);
  cov(2, 2) =
    (gt(GlobalTally::K_TRACKLENGTH, TallyResult::SUM_SQ) - n * kv[2] * kv[2]) /
    (n - 1);

  // Calculate covariances based on sums with Bessel's correction
  cov(0, 1) = (simulation::k_col_abs - n * kv[0] * kv[1]) / (n - 1);
  cov(0, 2) = (simulation::k_col_tra - n * kv[0] * kv[2]) / (n - 1);
  cov(1, 2) = (simulation::k_abs_tra - n * kv[1] * kv[2]) / (n - 1);
  cov(1, 0) = cov(0, 1);
  cov(2, 0) = cov(0, 2);
  cov(2, 1) = cov(1, 2);

  // Check to see if two estimators are the same; this is guaranteed to happen
  // in MG-mode with survival biasing when the collision and absorption
  // estimators are the same, but can theoretically happen at anytime.
  // If it does, the standard estimators will produce floating-point
  // exceptions and an expression specifically derived for the combination of
  // two estimators (vice three) should be used instead.

  // First we will identify if there are any matching estimators
  int i, j;
  bool use_three = false;
  if ((std::abs(kv[0] - kv[1]) / kv[0] < FP_REL_PRECISION) &&
      (std::abs(cov(0, 0) - cov(1, 1)) / cov(0, 0) < FP_REL_PRECISION)) {
    // 0 and 1 match, so only use 0 and 2 in our comparisons
    i = 0;
    j = 2;

  } else if ((std::abs(kv[0] - kv[2]) / kv[0] < FP_REL_PRECISION) &&
             (std::abs(cov(0, 0) - cov(2, 2)) / cov(0, 0) < FP_REL_PRECISION)) {
    // 0 and 2 match, so only use 0 and 1 in our comparisons
    i = 0;
    j = 1;

  } else if ((std::abs(kv[1] - kv[2]) / kv[1] < FP_REL_PRECISION) &&
             (std::abs(cov(1, 1) - cov(2, 2)) / cov(1, 1) < FP_REL_PRECISION)) {
    // 1 and 2 match, so only use 0 and 1 in our comparisons
    i = 0;
    j = 1;

  } else {
    // No two estimators match, so set boolean to use all three estimators.
    use_three = true;
  }

  if (use_three) {
    // Use three estimators as derived in the paper by Urbatsch

    // Initialize variables
    double g = 0.0;
    array<double, 3> S {};

    for (int l = 0; l < 3; ++l) {
      // Permutations of estimates
      int k;
      switch (l) {
      case 0:
        // i = collision, j = absorption, k = tracklength
        i = 0;
        j = 1;
        k = 2;
        break;
      case 1:
        // i = absortion, j = tracklength, k = collision
        i = 1;
        j = 2;
        k = 0;
        break;
      case 2:
        // i = tracklength, j = collision, k = absorption
        i = 2;
        j = 0;
        k = 1;
        break;
      }

      // Calculate weighting
      double f = cov(j, j) * (cov(k, k) - cov(i, k)) - cov(k, k) * cov(i, j) +
                 cov(j, k) * (cov(i, j) + cov(i, k) - cov(j, k));

      // Add to S sums for variance of combined estimate
      S[0] += f * cov(0, l);
      S[1] += (cov(j, j) + cov(k, k) - 2.0 * cov(j, k)) * kv[l] * kv[l];
      S[2] += (cov(k, k) + cov(i, j) - cov(j, k) - cov(i, k)) * kv[l] * kv[j];

      // Add to sum for combined k-effective
      k_combined[0] += f * kv[l];
      g += f;
    }

    // Complete calculations of S sums
    for (auto& S_i : S) {
      S_i *= (n - 1);
    }
    S[0] *= (n - 1) * (n - 1);

    // Calculate combined estimate of k-effective
    k_combined[0] /= g;

    // Calculate standard deviation of combined estimate
    g *= (n - 1) * (n - 1);
    k_combined[1] =
      std::sqrt(S[0] / (g * n * (n - 3)) * (1 + n * ((S[1] - 2 * S[2]) / g)));

  } else {
    // Use only two estimators
    // These equations are derived analogously to that done in the paper by
    // Urbatsch, but are simpler than for the three estimators case since the
    // block matrices of the three estimator equations reduces to scalars here

    // Store the commonly used term
    double f = kv[i] - kv[j];
    double g = cov(i, i) + cov(j, j) - 2.0 * cov(i, j);

    // Calculate combined estimate of k-effective
    k_combined[0] = kv[i] - (cov(i, i) - cov(i, j)) / g * f;

    // Calculate standard deviation of combined estimate
    k_combined[1] = (cov(i, i) * cov(j, j) - cov(i, j) * cov(i, j)) *
                    (g + n * f * f) / (n * (n - 2) * g * g);
    k_combined[1] = std::sqrt(k_combined[1]);
  }
  return 0;
}

void shannon_entropy()
{
  // Get source weight in each mesh bin
  bool sites_outside;
  xt::xtensor<double, 1> p =
    simulation::entropy_mesh->count_sites(simulation::fission_bank.data(),
      simulation::fission_bank.size(), &sites_outside);

  // display warning message if there were sites outside entropy box
  if (sites_outside) {
    if (mpi::master)
      warning("Fission source site(s) outside of entropy box.");
  }

  if (mpi::master) {
    // Normalize to total weight of bank sites
    p /= xt::sum(p);

    // Sum values to obtain Shannon entropy
    double H = 0.0;
    for (auto p_i : p) {
      if (p_i > 0.0) {
        H -= p_i * std::log2(p_i);
      }
    }

    // Add value to vector
    simulation::entropy.push_back(H);
  }
}

void ufs_count_sites()
{
  if (simulation::current_batch == 1 && simulation::current_gen == 1) {
    // On the first generation, just assume that the source is already evenly
    // distributed so that effectively the production of fission sites is not
    // biased

    std::size_t n = simulation::ufs_mesh->n_bins();
    double vol_frac = simulation::ufs_mesh->volume_frac_;
    simulation::source_frac = xt::xtensor<double, 1>({n}, vol_frac);

  } else {
    // count number of source sites in each ufs mesh cell
    bool sites_outside;
    simulation::source_frac =
      simulation::ufs_mesh->count_sites(simulation::source_bank.data(),
        simulation::source_bank.size(), &sites_outside);

    // Check for sites outside of the mesh
    if (mpi::master && sites_outside) {
      fatal_error("Source sites outside of the UFS mesh!");
    }

#ifdef OPENMC_MPI
    // Send source fraction to all processors
    int n_bins = simulation::ufs_mesh->n_bins();
    MPI_Bcast(
      simulation::source_frac.data(), n_bins, MPI_DOUBLE, 0, mpi::intracomm);
#endif

    // Normalize to total weight to get fraction of source in each cell
    double total = xt::sum(simulation::source_frac)();
    simulation::source_frac /= total;

    // Since the total starting weight is not equal to n_particles, we need to
    // renormalize the weight of the source sites
    for (int i = 0; i < simulation::work_per_rank; ++i) {
      simulation::source_bank[i].wgt *= settings::n_particles / total;
    }
  }
}

double ufs_get_weight(const Particle& p)
{
  // Determine indices on ufs mesh for current location
  int mesh_bin = simulation::ufs_mesh->get_bin(p.r());
  if (mesh_bin < 0) {
    p.write_restart();
    fatal_error("Source site outside UFS mesh!");
  }

  if (simulation::source_frac(mesh_bin) != 0.0) {
    return simulation::ufs_mesh->volume_frac_ /
           simulation::source_frac(mesh_bin);
  } else {
    return 1.0;
  }
}

void write_eigenvalue_hdf5(hid_t group)
{
  write_dataset(group, "n_inactive", settings::n_inactive);
  write_dataset(group, "generations_per_batch", settings::gen_per_batch);
  write_dataset(group, "k_generation", simulation::k_generation);
  if (settings::entropy_on) {
    write_dataset(group, "entropy", simulation::entropy);
  }
  write_dataset(group, "k_col_abs", simulation::k_col_abs);
  write_dataset(group, "k_col_tra", simulation::k_col_tra);
  write_dataset(group, "k_abs_tra", simulation::k_abs_tra);
  array<double, 2> k_combined;
  openmc_get_keff(k_combined.data());
  write_dataset(group, "k_combined", k_combined);

  // Write delayed neutron kinetics parameters if calculated
  if (settings::calculate_prompt_k) {
    write_dataset(group, "k_prompt_generation", simulation::k_prompt);
    array<double, 2> k_prompt_vals {
      simulation::keff_prompt, simulation::keff_prompt_std};
    write_dataset(group, "k_prompt", k_prompt_vals);
    array<double, 2> beta_eff_vals {
      simulation::beta_eff, simulation::beta_eff_std};
    write_dataset(group, "beta_eff", beta_eff_vals);

    // Write IFP-weighted alpha eigenvalue if calculated
    if (settings::calculate_alpha && settings::ifp_on) {
      array<double, 2> lambda_eff_ifp_vals {
        simulation::lambda_eff_ifp, simulation::lambda_eff_ifp_std};
      write_dataset(group, "lambda_eff_ifp", lambda_eff_ifp_vals);
      array<double, 2> alpha_ifp_vals {
        simulation::alpha_ifp, simulation::alpha_ifp_std};
      write_dataset(group, "alpha_ifp", alpha_ifp_vals);
    }
  }
}

void read_eigenvalue_hdf5(hid_t group)
{
  read_dataset(group, "generations_per_batch", settings::gen_per_batch);
  int n = simulation::restart_batch * settings::gen_per_batch;
  simulation::k_generation.resize(n);
  read_dataset(group, "k_generation", simulation::k_generation);
  if (settings::entropy_on) {
    read_dataset(group, "entropy", simulation::entropy);
  }
  read_dataset(group, "k_col_abs", simulation::k_col_abs);
  read_dataset(group, "k_col_tra", simulation::k_col_tra);
  read_dataset(group, "k_abs_tra", simulation::k_abs_tra);

  // Read delayed neutron kinetics parameters if they exist
  if (settings::calculate_prompt_k && object_exists(group, "k_prompt")) {
    simulation::k_prompt.resize(n);
    read_dataset(group, "k_prompt_generation", simulation::k_prompt);
    array<double, 2> k_prompt_vals;
    read_dataset(group, "k_prompt", k_prompt_vals);
    simulation::keff_prompt = k_prompt_vals[0];
    simulation::keff_prompt_std = k_prompt_vals[1];
    array<double, 2> beta_eff_vals;
    read_dataset(group, "beta_eff", beta_eff_vals);
    simulation::beta_eff = beta_eff_vals[0];
    simulation::beta_eff_std = beta_eff_vals[1];

    // Read IFP-weighted alpha eigenvalue if it exists
    if (settings::calculate_alpha && settings::ifp_on) {
      if (object_exists(group, "lambda_eff_ifp")) {
        array<double, 2> lambda_eff_ifp_vals;
        read_dataset(group, "lambda_eff_ifp", lambda_eff_ifp_vals);
        simulation::lambda_eff_ifp = lambda_eff_ifp_vals[0];
        simulation::lambda_eff_ifp_std = lambda_eff_ifp_vals[1];
      }
      if (object_exists(group, "alpha_ifp")) {
        array<double, 2> alpha_ifp_vals;
        read_dataset(group, "alpha_ifp", alpha_ifp_vals);
        simulation::alpha_ifp = alpha_ifp_vals[0];
        simulation::alpha_ifp_std = alpha_ifp_vals[1];
      }
    }
  }
}

void setup_kinetics_tallies()
{
  // Only create tallies if alpha calculations are enabled with IFP
  if (!settings::calculate_alpha || !settings::ifp_on)
    return;

  // Create internal tally for kinetics parameters
  auto* tally = Tally::create();
  simulation::kinetics_tally_index = tally->index();
  tally->set_writable(false); // Don't write to tallies.out

  // Use IFP scores for generation time (Λ_eff) calculation
  // β_eff is calculated from k-prompt instead of IFP
  // Formulas:
  //   β_eff = (k - k_prompt) / k
  //   Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
  //   α = (ρ - β_eff) / Λ_eff, where ρ = (k - 1) / k
  vector<std::string> scores;
  scores.push_back("ifp-time-numerator");  // Index 0: IFP-weighted lifetime numerator
  scores.push_back("ifp-denominator");     // Index 1: IFP common denominator

  tally->set_scores(scores);

  // Set nuclides to "total" (required for results array allocation)
  // -1 represents "total" in the nuclides array
  tally->set_nuclides({"total"});

  // No filters - tally over entire geometry
  tally->set_filters({});

  // Set ifp_parameter to GenerationTime since we only need Λ_eff from IFP
  // (β_eff is calculated from k-prompt). This is necessary for programmatically
  // created tallies because set_scores() doesn't automatically set ifp_parameter
  // like the XML-based tally constructor does.
  if (settings::ifp_parameter == IFPParameter::None) {
    settings::ifp_parameter = IFPParameter::GenerationTime;
  } else if (settings::ifp_parameter == IFPParameter::BetaEffective) {
    settings::ifp_parameter = IFPParameter::Both;
  }
}

} // namespace openmc
