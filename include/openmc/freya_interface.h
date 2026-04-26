#ifndef OPENMC_FREYA_INTERFACE_H
#define OPENMC_FREYA_INTERFACE_H

#ifdef OPENMC_USE_FISSION_LIB

#include <cstdint>

namespace openmc {

//! \brief Thin wrapper around the LLNL Fission Library (FREYA).
//!
//! Only compiled when OPENMC_USE_FISSION_LIB is defined. The FREYA C API uses
//! a global fissionEvent pointer and is NOT thread-safe — callers must hold a
//! lock (e.g. an `omp critical(freya_event)` section) around each generate +
//! retrieve cycle. set_seed() stores the current OpenMC LCG seed pointer so
//! that FREYA's RNG callback advances the same stream as the rest of OpenMC.
namespace freya {

//! Initialise FREYA. Idempotent (std::call_once internally) and safe to call
//! before every fission event.
//!
//! \param[in] data_path  Directory containing FREYA data files. If null or
//!                       empty, falls back to ``$FREYA_DATA_PATH`` and then to
//!                       the compile-time default.
void init(const char* data_path = nullptr);

//! Point the FREYA RNG callback at this seed before each FREYA call. Must be
//! called inside the FREYA critical section.
void set_seed(uint64_t* seed);

//! True if the FREYA library was successfully initialised.
bool is_initialized();

} // namespace freya
} // namespace openmc

#endif // OPENMC_USE_FISSION_LIB
#endif // OPENMC_FREYA_INTERFACE_H
