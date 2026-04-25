# FindFissionLib.cmake
#
# Finds the LLNL Fission Library (libFission), which provides the FREYA
# correlated fission model and Spriggs 8-group delayed neutron sampling.
#
# Usage:
#   cmake -DOPENMC_USE_FREYA=ON \
#         -DFISSION_LIB_DIR=/path/to/fission_v2.0.5 ..
#
# Variables set by this module:
#   FissionLib_FOUND          -- TRUE if the library was found
#   FissionLib_INCLUDE_DIRS   -- Directory containing fissionEvent.h
#   FissionLib_LIBRARIES      -- Path to libFission.so (or .a)
#
# Imported target:
#   FissionLib::Fission        -- Use with target_link_libraries()
#
# Search hints (in order):
#   1. FISSION_LIB_DIR  CMake variable or environment variable
#   2. Standard system paths (/usr/local, /usr)
#   3. The fission_lib_extract directory in this repository

find_path(FissionLib_INCLUDE_DIR
  NAMES fissionEvent.h
  HINTS
    ${FISSION_LIB_DIR}
    ${FISSION_LIB_DIR}/include
    $ENV{FISSION_LIB_DIR}
    $ENV{FISSION_LIB_DIR}/include
    ${CMAKE_SOURCE_DIR}/fission_lib_extract/fission_v2.0.5/include
  PATH_SUFFIXES include fission_lib/include
  DOC "Directory containing fissionEvent.h"
)

find_library(FissionLib_LIBRARY
  NAMES Fission
  HINTS
    ${FISSION_LIB_DIR}
    ${FISSION_LIB_DIR}/lib
    $ENV{FISSION_LIB_DIR}
    $ENV{FISSION_LIB_DIR}/lib
    ${CMAKE_SOURCE_DIR}/fission_lib_extract/fission_v2.0.5/lib
  PATH_SUFFIXES lib
  DOC "Path to libFission shared library"
)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(FissionLib
  REQUIRED_VARS FissionLib_LIBRARY FissionLib_INCLUDE_DIR
  FAIL_MESSAGE
    "LLNL Fission Library not found. Set -DFISSION_LIB_DIR=/path/to/fission_v2.0.5 "
    "and ensure 'make install' has been run in that directory."
)

if(FissionLib_FOUND)
  set(FissionLib_LIBRARIES    ${FissionLib_LIBRARY})
  set(FissionLib_INCLUDE_DIRS ${FissionLib_INCLUDE_DIR})

  if(NOT TARGET FissionLib::Fission)
    add_library(FissionLib::Fission SHARED IMPORTED)
    set_target_properties(FissionLib::Fission PROPERTIES
      IMPORTED_LOCATION             "${FissionLib_LIBRARY}"
      INTERFACE_INCLUDE_DIRECTORIES "${FissionLib_INCLUDE_DIR}"
    )
  endif()
endif()

mark_as_advanced(FissionLib_INCLUDE_DIR FissionLib_LIBRARY)
