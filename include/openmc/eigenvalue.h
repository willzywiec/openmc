//! \file eigenvalue.h
//! \brief Data/functions related to k-eigenvalue calculations

#ifndef OPENMC_EIGENVALUE_H
#define OPENMC_EIGENVALUE_H

#include <algorithm>
#include <cmath>
#include <cstdint> // for int64_t

#include "xtensor/xtensor.hpp"
#include <hdf5.h>

#include "openmc/array.h"
#include "openmc/particle.h"
#include "openmc/vector.h"

namespace openmc {

//==============================================================================
// Time-dependent fission tally for alpha eigenvalue extraction
//==============================================================================

//! \class TimeFissionTally
//! \brief Accumulates fission events in time bins for exponential fit
struct TimeFissionTally {
  vector<double> bin_edges;     //!< Time bin edges [seconds]
  vector<double> bin_counts;    //!< Accumulated ν×weight per bin
  vector<double> bin_counts_sq; //!< For variance calculation
  int n_samples {0};            //!< Number of samples accumulated

  //! Initialize time bins
  //! \param n_bins Number of time bins
  //! \param t_min Minimum time [s]
  //! \param t_max Maximum time [s]
  //! \param logarithmic Use logarithmic bin spacing if true
  void initialize(int n_bins, double t_min, double t_max, bool logarithmic);

  //! Score a fission event to the appropriate time bin
  //! \param time Absolute time of fission event [s]
  //! \param nu_weight ν × weight contribution
  void score(double time, double nu_weight);

  //! Reset all bin counts
  void reset();

  //! Find the bin index for a given time
  //! \param time Time value [s]
  //! \return Bin index, or -1 if outside range
  int find_bin(double time) const;
};

//==============================================================================
// Global variables
//==============================================================================

namespace simulation {

extern double keff_generation; //!<  Single-generation k on each processor
extern array<double, 2> k_sum; //!< Used to reduce sum and sum_sq
extern vector<double> entropy; //!< Shannon entropy at each generation
extern xt::xtensor<double, 1> source_frac; //!< Source fraction for UFS

// Delayed neutron kinetics parameters
extern double keff_prompt_generation; //!< Single-generation k_prompt
extern vector<double> k_prompt;       //!< k_prompt for each generation
extern double keff_prompt;            //!< Mean k_prompt over active generations
extern double keff_prompt_std;        //!< Standard deviation of k_prompt
extern double beta_eff;               //!< Effective delayed neutron fraction
extern double beta_eff_std;           //!< Standard deviation of beta_eff

// Alpha eigenvalue from direct flux-weighted method
extern double alpha;           //!< α = (ρ - β) / Λ
extern double alpha_std;       //!< Standard deviation of alpha

// IFP-weighted alpha eigenvalue
extern double alpha_ifp;              //!< α from IFP-weighted Λ_eff
extern double alpha_ifp_std;          //!< Standard deviation of α_ifp
extern double lambda_eff_ifp;         //!< IFP-weighted generation time Λ_eff [s]
extern double lambda_eff_ifp_std;     //!< Standard deviation of Λ_eff

// Time-dependent alpha eigenvalue
extern double alpha_time_dependent;       //!< α from time-dependent fit
extern double alpha_time_dependent_std;   //!< Standard deviation
extern double lambda_eff_time;            //!< Λ_eff derived from time-dep α [s]
extern double lambda_eff_time_std;        //!< Standard deviation

// Time-dependent fission tally
extern TimeFissionTally time_fission_tally;

// Neutron timing parameters
extern double prompt_neutron_lifetime;     //!< Prompt neutron lifetime ℓ (time to any removal) [s]
extern double prompt_neutron_lifetime_std; //!< Std dev of prompt neutron lifetime
extern double mean_generation_time;        //!< Mean generation time Λ (time to fission) [s]
extern double mean_generation_time_std;    //!< Std dev of mean generation time
extern int kinetics_tally_index;   //!< Index of internal kinetics tally

} // namespace simulation

//==============================================================================
// Non-member functions
//==============================================================================

//! Collect/normalize the tracklength keff from each process
void calculate_generation_keff();

//! Collect/normalize the tracklength k_prompt from each process
void calculate_generation_prompt_keff();

//! Calculate mean/standard deviation of keff during active generations
//!
//! This function sets the global variables keff and keff_std which represent
//! the mean and standard deviation of the mean of k-effective over active
//! generations. It also broadcasts the value from the master process.
void calculate_average_keff();

//! Calculate delayed neutron kinetics parameters
//!
//! This function calculates k_prompt, beta_eff, and alpha eigenvalues
//! over active generations. Results are stored in simulation namespace.
void calculate_kinetics_parameters();

//! Setup internal tallies for alpha eigenvalue calculations
//!
//! Creates tallies with prompt chain scores needed for alpha calculations
void setup_kinetics_tallies();

//! Initialize time-dependent alpha tally
//!
//! Sets up time bins for fission event accumulation
void initialize_time_alpha_tally();

//! Extract alpha eigenvalue from time-dependent fission rate
//!
//! Performs weighted linear regression on ln(F) vs t to extract α
//! \param tally The time fission tally with accumulated data
//! \return The alpha eigenvalue [/s]
double extract_alpha_from_time_tally(const TimeFissionTally& tally);

//! Calculates a minimum variance estimate of k-effective
//!
//! The minimum variance estimate is based on a linear combination of the
//! collision, absorption, and tracklength estimates. The theory behind this can
//! be found in M. Halperin, "Almost linearly-optimum combination of unbiased
//! estimates," J. Am. Stat. Assoc., 56, 36-43 (1961),
//! doi:10.1080/01621459.1961.10482088. The implementation here follows that
//! described in T. Urbatsch et al., "Estimation and interpretation of keff
//! confidence intervals in MCNP," Nucl. Technol., 111, 169-182 (1995).
//!
//! \param[out] k_combined Estimate of k-effective and its standard deviation
//! \return Error status
extern "C" int openmc_get_keff(double* k_combined);

//! Sample/redistribute source sites from accumulated fission sites
void synchronize_bank();

//! Calculates the Shannon entropy of the fission source distribution to assess
//! source convergence
void shannon_entropy();

//! Determines the source fraction in each UFS mesh cell and reweights the
//! source bank so that the sum of the weights is equal to n_particles. The
//! 'source_frac' variable is used later to bias the production of fission sites
void ufs_count_sites();

//! Get UFS weight corresponding to particle's location
double ufs_get_weight(const Particle& p);

//! Write data related to k-eigenvalue to statepoint
//! \param[in] group HDF5 group
void write_eigenvalue_hdf5(hid_t group);

//! Read data related to k-eigenvalue from statepoint
//! \param[in] group HDF5 group
void read_eigenvalue_hdf5(hid_t group);

} // namespace openmc

#endif // OPENMC_EIGENVALUE_H
