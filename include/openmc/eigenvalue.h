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

// IFP-weighted generation times and alpha eigenvalue
// Λ_eff = ifp-time-numerator / (ifp-denominator × k_eff)
// Λ_p = ifp-prompt-time-numerator / (ifp-prompt-denominator × k_eff)
// α_dc = −β_eff / (Λ_p · k_p),  α = (k_p − 1) / (Λ_p · k_p)
extern double alpha_dc_ifp;           //!< α at delayed critical from IFP-weighted Λ_p [/s]
extern double alpha_dc_ifp_std;      //!< Standard deviation of α_dc_ifp
extern double alpha_ifp;              //!< α at actual reactivity state [/s]
extern double alpha_ifp_std;          //!< Standard deviation of α_ifp
extern double lambda_eff_ifp;         //!< IFP-weighted generation time Λ_eff [s]
extern double lambda_eff_ifp_std;     //!< Standard deviation of Λ_eff
extern double lambda_p_ifp;           //!< IFP-weighted prompt generation time Λ_p [s]
extern double lambda_p_ifp_std;       //!< Standard deviation of Λ_p

// Index of internal kinetics tally (for alpha calculations using IFP scores)
extern int kinetics_tally_index;

// Accumulators for k_prompt statistics
extern double k_prompt_sum;
extern double k_prompt_sum_sq;

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
//! This function calculates k_prompt, beta_eff, and alpha eigenvalue
//! over active generations. Results are stored in simulation namespace.
void calculate_kinetics_parameters();

//! Setup internal tallies for alpha eigenvalue calculations
//!
//! Creates a tally with IFP scores needed for alpha calculation
void setup_kinetics_tallies();

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
