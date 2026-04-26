#ifdef OPENMC_USE_FISSION_LIB

#include "openmc/freya_interface.h"
#include "openmc/random_lcg.h"   // prn()
#include "openmc/error.h"        // write_message()

// FREYA must be defined to expose setfreyadatapath_ and getfreya_errors_
// (they are inside #ifdef FREYA guards in Fission.h).
#ifndef FREYA
#define FREYA
#endif
#include "Fission.h"

#include <cstdlib>   // getenv
#include <cstring>
#include <mutex>

// Default data path set by CMake; runtime $FREYA_DATA_PATH overrides it.
#ifndef FREYA_DATA_DEFAULT_PATH
#define FREYA_DATA_DEFAULT_PATH ""
#endif

namespace openmc {
namespace freya {

namespace {

// Translation-unit-local state.
bool initialized = false;
std::once_flag init_flag;

// Per-thread seed pointer: set before each genfissevt_() call so the RNG
// callback advances the same LCG stream as the rest of OpenMC.
thread_local uint64_t* seed_ptr = nullptr;

// RNG callback registered with FREYA via setrngd_().
// Must have signature: double (*)(void).
double rng_callback()
{
  return prn(seed_ptr);
}

} // anonymous namespace

void init(const char* data_path)
{
  std::call_once(init_flag, [data_path]() {
    // Resolve data directory
    const char* path = data_path;
    if (!path || path[0] == '\0')
      path = std::getenv("FREYA_DATA_PATH");
    if (!path || path[0] == '\0')
      path = FREYA_DATA_DEFAULT_PATH;

    if (path && path[0] != '\0') {
      // setfreyadatapath_ modifies its argument (Fortran string), so copy it.
      char buf[4096];
      std::strncpy(buf, path, sizeof(buf) - 1);
      buf[sizeof(buf) - 1] = '\0';
      setfreyadatapath_(buf);
    }

    // Bind OpenMC's LCG to FREYA
    setrngd_(rng_callback);

    // Enable full FREYA correlated fission model (correlation option 3).
    // For isotopes not in FREYA the library reverts to option 0 automatically.
    int correl = 3;
    setcorrel_(&correl);

    // Prompt neutrons and photons only; delayed neutrons handled by Spriggs+GEF.
    int delay = 0;
    setdelay_(&delay);

    initialized = true;

    write_message("FREYA correlated fission model initialized.", 6);
    if (path && path[0] != '\0')
      write_message(std::string("FREYA data path: ") + path, 6);
  });
}

void set_seed(uint64_t* seed)
{
  seed_ptr = seed;
}

bool is_initialized()
{
  return initialized;
}

} // namespace freya
} // namespace openmc

#endif // OPENMC_USE_FISSION_LIB
