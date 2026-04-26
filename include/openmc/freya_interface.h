/* freya_interface.h
 *
 * Thin wrapper around the LLNL Fission Library (FREYA) for use in OpenMC.
 * Only compiled when OPENMC_USE_FISSION_LIB is defined.
 *
 * Initialization:
 *   Call freya_init() once before any fission event generation.
 *   Data path: $FREYA_DATA_PATH env var, or the compiled-in default.
 *
 * Thread safety:
 *   The FREYA C API uses a global fissionEvent pointer and is NOT thread-safe.
 *   Callers must hold a lock (freya_lock) around each generate + retrieve cycle.
 *   freya_set_seed() stores the current OpenMC LCG seed pointer so that the
 *   FREYA RNG callback (freya_rng_callback) advances the same stream.
 */

#ifndef OPENMC_FREYA_INTERFACE_H
#define OPENMC_FREYA_INTERFACE_H

#ifdef OPENMC_USE_FISSION_LIB

#include <cstdint>

namespace openmc {
namespace freya {

// Initialise FREYA (call once at simulation start).
// data_path: directory containing FREYA data files.
//   NULL → use $FREYA_DATA_PATH env var → compiled-in default.
void init(const char* data_path = nullptr);

// Point the FREYA RNG callback at this seed before each FREYA call.
// Must be called inside the freya_lock critical section.
void set_seed(uint64_t* seed);

// True if the FREYA library was successfully initialized.
bool is_initialized();

} // namespace freya
} // namespace openmc

#endif // OPENMC_USE_FISSION_LIB
#endif // OPENMC_FREYA_INTERFACE_H
