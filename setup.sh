#!/bin/bash
################################################################################
# OpenMC Installation and Setup Script
################################################################################
# This script automates the installation and configuration of OpenMC,
# including setting up cross section data paths, building the code, setting up
# a Python virtual environment, and installing the Python API.
#
# Author: William Zywiec (willzywiec@gmail.com)
#
# Usage: bash setup.sh [OPTIONS]
#        ./setup.sh [OPTIONS]
#
# Note: Do NOT use "source setup.sh" -- this script must be executed, not
#       sourced. If you get "Permission denied", use: bash setup.sh
#
# Options:
#   --xs-dir PATH        Path to cross section data directory (default: ../endfb80-hdf5)
#   --skip-xs            Skip cross section data setup
#   --with-mpi           Build with MPI support
#   --with-fission-lib   Build the vendored LLNL Fission Library (FREYA / GEF /
#                        Spriggs) and link OpenMC against it. Requires gfortran.
#                        Enables: openmc.FreyaSFSource, settings.freya_analog,
#                        Spriggs 8-group delayed neutrons, GEF SF spectra.
#   --build-type         Set build type (Debug|Release|RelWithDebInfo)
#   --force-submodules   Force re-download of vendor submodules (fixes corrupted state)
#   --help               Show this help message
################################################################################

# Fix Windows/WSL line endings at runtime if this file has CRLF
if [[ "$(printf 'x\r')" == "x"$'\r' ]] 2>/dev/null; then
    # We're in bash -- check if this script has CRLF line endings
    if head -1 "$0" 2>/dev/null | grep -q $'\r'; then
        echo "Fixing Windows line endings in setup.sh..."
        SELF="$(realpath "$0" 2>/dev/null || readlink -f "$0" 2>/dev/null || echo "$0")"
        sed -i 's/\r$//' "$SELF"
        exec bash "$SELF" "$@"
    fi
fi

# Prevent sourcing -- this script should be executed, not sourced
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
    echo "Error: This script should not be sourced. Run it instead:"
    echo "  bash setup.sh [OPTIONS]"
    echo "  ./setup.sh [OPTIONS]"
    return 1 2>/dev/null || exit 1
fi

set -e  # Exit on error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default options
SKIP_XS=false
WITH_MPI=false
WITH_FISSION_LIB=false
BUILD_TYPE="RelWithDebInfo"
INSTALL_PREFIX="${HOME}/.local"
XS_DIR=""  # Will be set to default after SCRIPT_DIR is determined
FORCE_SUBMODULES=false

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Default cross section directory (sibling to openmc directory)
DEFAULT_XS_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/endfb80-hdf5"

################################################################################
# Helper functions
################################################################################

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_usage() {
    sed -n '/^# Usage:/,/^##/{ /^##/d; s/^# \?//; p }' "$0"
}

################################################################################
# Parse command line arguments
################################################################################

while [[ $# -gt 0 ]]; do
    case $1 in
        --xs-dir)
            XS_DIR="$2"
            shift 2
            ;;
        --skip-xs)
            SKIP_XS=true
            shift
            ;;
        --with-mpi)
            WITH_MPI=true
            shift
            ;;
        --with-fission-lib)
            WITH_FISSION_LIB=true
            shift
            ;;
        --build-type)
            BUILD_TYPE="$2"
            shift 2
            ;;
        --install-prefix)
            INSTALL_PREFIX="$2"
            shift 2
            ;;
        --force-submodules)
            FORCE_SUBMODULES=true
            shift
            ;;
        --help)
            print_usage
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            print_usage
            exit 1
            ;;
    esac
done

################################################################################
# Check prerequisites
################################################################################

log_info "Checking prerequisites..."

# Check if we're in the OpenMC directory
if [[ ! -f "${SCRIPT_DIR}/CMakeLists.txt" ]] || [[ ! -d "${SCRIPT_DIR}/src" ]]; then
    log_error "This script must be run from the OpenMC root directory"
    exit 1
fi

# Check for CMake
if ! command -v cmake &> /dev/null; then
    log_error "CMake is required but not found"
    exit 1
fi
CMAKE_VERSION=$(cmake --version | head -n1 | awk '{print $3}')
log_info "Found CMake ${CMAKE_VERSION}"

# Check for Python
if ! command -v python3 &> /dev/null; then
    log_error "Python 3 is required but not found"
    exit 1
fi
PYTHON_VERSION=$(python3 --version | awk '{print $2}')
log_info "Found Python ${PYTHON_VERSION}"

# Check for HDF5 development libraries
HDF5_FOUND=false
if pkg-config --exists hdf5 2>/dev/null; then
    HDF5_FOUND=true
elif [[ -f "/usr/include/hdf5.h" ]] || [[ -f "/usr/local/include/hdf5.h" ]] || \
     [[ -d "/usr/include/hdf5" ]] || [[ -d "/usr/local/include/hdf5" ]]; then
    HDF5_FOUND=true
elif ldconfig -p 2>/dev/null | grep -q libhdf5; then
    HDF5_FOUND=true
fi

if [[ "${HDF5_FOUND}" == true ]]; then
    log_info "Found HDF5 development libraries"
else
    log_warning "HDF5 development libraries not detected (CMake will check during configuration)"
fi

################################################################################
# Initialize git submodules
################################################################################

log_info "Checking vendor dependencies..."

# Check if git is available
if ! command -v git &> /dev/null; then
    log_error "Git is required but not found"
    exit 1
fi

# Function to clone a vendor dependency directly (fallback for corrupted submodules)
clone_vendor_dep() {
    local name="$1"
    local url="$2"
    local tag="$3"
    local dest="${SCRIPT_DIR}/vendor/${name}"

    log_info "Cloning ${name} from ${url}..."

    # Remove existing directory with multiple fallback approaches
    if [[ -d "${dest}" ]]; then
        # First, try to fix permissions (git submodules often have restrictive perms)
        chmod -R u+rwX "${dest}" 2>/dev/null || true
        # Remove any git index lock files
        rm -f "${dest}/.git/index.lock" 2>/dev/null || true
        # Try standard removal
        rm -rf "${dest}" 2>/dev/null
        # If still exists, try with sudo or more aggressive approach
        if [[ -d "${dest}" ]]; then
            log_warning "Standard removal failed for ${dest}, trying alternative methods..."
            # Try removing contents first, then directory
            find "${dest}" -type f -exec rm -f {} \; 2>/dev/null || true
            find "${dest}" -type d -empty -delete 2>/dev/null || true
            rm -rf "${dest}" 2>/dev/null || true
        fi
        # Final check
        if [[ -d "${dest}" ]]; then
            log_error "Cannot remove existing directory ${dest}"
            log_error "Please manually remove it with: sudo rm -rf ${dest}"
            return 1
        fi
    fi

    if git clone --depth 1 --branch "${tag}" "${url}" "${dest}"; then
        rm -rf "${dest}/.git"  # Remove .git to avoid submodule conflicts
        log_success "Successfully cloned ${name} ${tag}"
        return 0
    else
        log_error "Failed to clone ${name}"
        return 1
    fi
}

# Initialize and update git submodules
cd "${SCRIPT_DIR}"
if [[ -d ".git" ]]; then
    # Force re-download if requested
    if [[ "${FORCE_SUBMODULES}" == true ]]; then
        log_warning "Force submodule mode: removing and re-downloading vendor dependencies..."
        for dep in xtl xtensor pugixml fmt Catch2; do
            rm -rf "${SCRIPT_DIR}/vendor/${dep}"
        done
        git submodule deinit -f --all 2>/dev/null || true
    fi

    log_info "Initializing git submodules..."
    if ! git submodule update --init --recursive; then
        log_warning "Standard submodule update failed, trying with force..."
        if ! git submodule update --init --recursive --force; then
            log_warning "Submodule update failed. Attempting direct clone fallback..."
            SUBMODULE_FAILED=true
        fi
    fi

    # Check if submodules are still empty and use direct clone as fallback
    # Must check for actual header files, not just directories
    NEED_FALLBACK=false
    if [[ ! -f "${SCRIPT_DIR}/vendor/xtl/include/xtl/xbasic_fixed_string.hpp" ]]; then
        log_warning "xtl headers not found after submodule update"
        NEED_FALLBACK=true
    fi
    if [[ ! -f "${SCRIPT_DIR}/vendor/xtensor/include/xtensor/xtensor.hpp" ]]; then
        log_warning "xtensor headers not found after submodule update"
        NEED_FALLBACK=true
    fi

    if [[ "${NEED_FALLBACK}" == true ]] || [[ "${SUBMODULE_FAILED:-false}" == true ]]; then
        log_warning "Submodules appear corrupted. Using direct clone fallback..."

        # Clone with specific compatible versions
        # Note: xtensor 0.25.0 requires xvariant.hpp which was removed in xtl 0.8.0
        # So we use xtl 0.7.7 (last version with xvariant.hpp) with xtensor 0.25.0
        clone_vendor_dep "xtl" "https://github.com/xtensor-stack/xtl.git" "0.7.7" || exit 1
        clone_vendor_dep "xtensor" "https://github.com/xtensor-stack/xtensor.git" "0.25.0" || exit 1
        clone_vendor_dep "pugixml" "https://github.com/zeux/pugixml.git" "latest" || \
            clone_vendor_dep "pugixml" "https://github.com/zeux/pugixml.git" "v1.14" || exit 1
        clone_vendor_dep "fmt" "https://github.com/fmtlib/fmt.git" "11.0.2" || exit 1
        clone_vendor_dep "Catch2" "https://github.com/catchorg/Catch2.git" "v3.3.2" || exit 1

        log_success "Vendor dependencies cloned via fallback method"
    else
        log_success "Git submodules initialized"
    fi
else
    log_warning "Not a git repository, skipping submodule initialization"
fi

# Verify critical vendor dependencies exist and have include directories
VENDOR_DEPS=("xtl" "xtensor" "pugixml" "fmt" "Catch2")
for dep in "${VENDOR_DEPS[@]}"; do
    DEP_DIR="${SCRIPT_DIR}/vendor/${dep}"
    # Check if directory exists and has content (more than just . and ..)
    if [[ ! -d "${DEP_DIR}" ]] || [[ -z "$(ls -A "${DEP_DIR}" 2>/dev/null)" ]]; then
        log_error "Vendor dependency '${dep}' not found or empty at ${DEP_DIR}"
        log_error "Try running with --force-submodules to fix:"
        log_error "  ./setup.sh --force-submodules --skip-xs"
        exit 1
    fi
    # Extra check for header-only libraries - verify actual header files exist
    if [[ "${dep}" == "xtl" ]]; then
        if [[ ! -f "${DEP_DIR}/include/xtl/xbasic_fixed_string.hpp" ]]; then
            log_error "Vendor dependency 'xtl' is missing header files"
            log_error "Try running with --force-submodules to fix:"
            log_error "  ./setup.sh --force-submodules --skip-xs"
            exit 1
        fi
    fi
    if [[ "${dep}" == "xtensor" ]]; then
        if [[ ! -f "${DEP_DIR}/include/xtensor/xtensor.hpp" ]]; then
            log_error "Vendor dependency 'xtensor' is missing header files"
            log_error "Try running with --force-submodules to fix:"
            log_error "  ./setup.sh --force-submodules --skip-xs"
            exit 1
        fi
    fi
    log_info "Found ${dep} (verified)"
done

log_success "Vendor dependencies ready"

################################################################################
# Setup cross section data
################################################################################

if [[ "$SKIP_XS" == false ]]; then
    log_info "Setting up cross section data..."

    # Use specified XS_DIR or default to sibling directory
    if [[ -z "${XS_DIR}" ]]; then
        XS_DATA_DIR="${DEFAULT_XS_DIR}"
    else
        # Resolve to absolute path
        XS_DATA_DIR="$(cd "$(dirname "${XS_DIR}")" && pwd)/$(basename "${XS_DIR}")"
    fi

    # Verify cross section data exists
    if [[ -d "${XS_DATA_DIR}" ]]; then
        if [[ -f "${XS_DATA_DIR}/cross_sections.xml" ]]; then
            log_success "Cross section data found at ${XS_DATA_DIR}"
        else
            log_error "cross_sections.xml not found in ${XS_DATA_DIR}"
            exit 1
        fi
    else
        log_error "Cross section directory not found: ${XS_DATA_DIR}"
        log_error "Please ensure the endfb80-hdf5 data is available, or specify with --xs-dir"
        exit 1
    fi
else
    log_info "Skipping cross section data setup"
    # Still need XS_DATA_DIR for environment script
    if [[ -z "${XS_DIR}" ]]; then
        XS_DATA_DIR="${DEFAULT_XS_DIR}"
    else
        XS_DATA_DIR="$(cd "$(dirname "${XS_DIR}")" && pwd)/$(basename "${XS_DIR}")"
    fi
fi

################################################################################
# Build the vendored LLNL Fission Library (optional)
################################################################################
#
# When --with-fission-lib is set, build fission_lib_extract/fission_v2.0.5/
# first. Its Makefile produces lib/libFission.{so,a} which OpenMC's
# FindFissionLib.cmake auto-discovers under fission_lib_extract/.
#
# Idempotent: skips if a freshly-built libFission already exists.

FISSION_LIB_ROOT="${SCRIPT_DIR}/fission_lib_extract/fission_v2.0.5"
FISSION_LIB_FOUND=""

if [[ "${WITH_FISSION_LIB}" == true ]]; then
    log_info "FREYA / fission library build requested..."

    if [[ ! -d "${FISSION_LIB_ROOT}" ]]; then
        log_error "Fission library source not found at ${FISSION_LIB_ROOT}"
        log_error "Expected fission_lib_extract/fission_v2.0.5/ in this repo."
        exit 1
    fi

    # Fortran compiler is required — fission lib's CMake disables FREYA without it.
    if ! command -v gfortran &> /dev/null; then
        log_error "--with-fission-lib requires gfortran (FREYA needs a Fortran compiler)."
        log_error "Install with: apt-get install gfortran   (or your distro equivalent)"
        exit 1
    fi
    log_info "Found gfortran: $(which gfortran)"

    # Reuse a previous build if libFission is already present.
    for ext in so dylib a; do
        if [[ -f "${FISSION_LIB_ROOT}/lib/libFission.${ext}" ]]; then
            FISSION_LIB_FOUND="${FISSION_LIB_ROOT}/lib/libFission.${ext}"
            break
        fi
    done

    if [[ -n "${FISSION_LIB_FOUND}" ]]; then
        log_info "Reusing existing libFission at ${FISSION_LIB_FOUND}"
    else
        log_info "Building libFission (this can take a few minutes the first time)..."
        (
            cd "${FISSION_LIB_ROOT}"
            # The bundled Makefile drives a CMake build inside ./build and installs
            # to ./lib. It hard-codes CXX/CC to whichever g++/gcc are on PATH.
            make
        ) || {
            log_error "Fission library build failed."
            log_error "Check ${FISSION_LIB_ROOT}/build/ for compiler logs."
            exit 1
        }

        for ext in so dylib a; do
            if [[ -f "${FISSION_LIB_ROOT}/lib/libFission.${ext}" ]]; then
                FISSION_LIB_FOUND="${FISSION_LIB_ROOT}/lib/libFission.${ext}"
                break
            fi
        done
        if [[ -z "${FISSION_LIB_FOUND}" ]]; then
            log_error "Fission library built without producing libFission.{so,dylib,a}."
            log_error "Inspect ${FISSION_LIB_ROOT}/build/ to diagnose."
            exit 1
        fi
        log_success "Built libFission: ${FISSION_LIB_FOUND}"
    fi
fi

################################################################################
# Build OpenMC
################################################################################

log_info "Building OpenMC..."

# Create build directory
BUILD_DIR="${SCRIPT_DIR}/build"
if [[ -d "${BUILD_DIR}" ]]; then
    log_info "Removing existing build directory"
    rm -rf "${BUILD_DIR}"
fi
mkdir -p "${BUILD_DIR}"

# Configure CMake
log_info "Configuring CMake (build type: ${BUILD_TYPE})..."
cd "${BUILD_DIR}"

CMAKE_OPTIONS=(
    "-DCMAKE_BUILD_TYPE=${BUILD_TYPE}"
    "-DCMAKE_INSTALL_PREFIX=${INSTALL_PREFIX}"
)

if [[ "$WITH_MPI" == true ]]; then
    CMAKE_OPTIONS+=("-DOPENMC_USE_MPI=ON")
    log_info "MPI support enabled"
fi

if [[ "${WITH_FISSION_LIB}" == true ]]; then
    CMAKE_OPTIONS+=("-DOPENMC_USE_FISSION_LIB=ON")
    log_info "FREYA / Fission Library support enabled"
fi

cmake "${CMAKE_OPTIONS[@]}" ..

# Build
log_info "Compiling OpenMC..."
make -j$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 2)

# Install
log_info "Installing OpenMC to ${INSTALL_PREFIX}..."
make install

log_success "OpenMC compiled and installed"

################################################################################
# Setup Python virtual environment and install OpenMC Python API
################################################################################

log_info "Setting up Python virtual environment..."

cd "${SCRIPT_DIR}"

# Fix for RHEL/CentOS where Python 3.12 installs to lib64 but looks in lib
# Try to create a symlink first (permanent fix), fall back to environment variables
PYTHON_LIB64_FIX=false
if [[ -d "/usr/lib64/python3.12" ]] && [[ ! -e "/usr/lib/python3.12" ]]; then
    log_info "Detected Python 3.12 lib64 installation..."
    # Try to create symlink (requires write permission to /usr/lib)
    if sudo ln -sf /usr/lib64/python3.12 /usr/lib/python3.12 2>/dev/null; then
        log_success "Created symlink /usr/lib/python3.12 -> /usr/lib64/python3.12"
        PYTHON_LIB64_FIX=true
    elif ln -sf /usr/lib64/python3.12 /usr/lib/python3.12 2>/dev/null; then
        log_success "Created symlink /usr/lib/python3.12 -> /usr/lib64/python3.12"
        PYTHON_LIB64_FIX=true
    else
        log_warning "Cannot create symlink (no write permission to /usr/lib)"
        log_warning "Python virtual environment may not work correctly"
        log_warning "Ask your sysadmin to run: sudo ln -sf /usr/lib64/python3.12 /usr/lib/python3.12"
    fi
fi

# If symlink exists or was created, Python should work without env vars
# Otherwise we need them but venv won't work properly
if [[ -L "/usr/lib/python3.12" ]] || [[ -d "/usr/lib/python3.12" ]]; then
    PYTHON_LIB64_FIX=true
fi

# Create virtual environment if it doesn't exist or is broken
VENV_DIR="${SCRIPT_DIR}/.env"
if [[ ! -f "${VENV_DIR}/bin/activate" ]]; then
    # Remove broken venv if it exists
    [[ -d "${VENV_DIR}" ]] && rm -rf "${VENV_DIR}"

    log_info "Creating Python virtual environment at ${VENV_DIR}..."

    # Try creating venv normally first
    if ! python3 -m venv "${VENV_DIR}" 2>/dev/null; then
        log_warning "Standard venv creation failed, trying without pip..."
        # Create without pip to avoid subprocess issues on some systems
        if ! python3 -m venv --without-pip "${VENV_DIR}" 2>/dev/null; then
            log_error "Failed to create Python virtual environment"
            log_warning "Continuing without Python bindings..."
            SKIP_PYTHON=true
        fi
    fi

    if [[ "${SKIP_PYTHON}" != true ]]; then
        log_success "Virtual environment created"
    fi
else
    log_info "Virtual environment already exists at ${VENV_DIR}"
fi

# Skip Python setup if venv creation failed
if [[ "${SKIP_PYTHON}" != true ]]; then
    # Activate virtual environment
    log_info "Activating virtual environment..."
    source "${VENV_DIR}/bin/activate"

    # Check if pip is available, if not bootstrap it
    if ! python -m pip --version &>/dev/null; then
        log_info "Bootstrapping pip..."
        curl -sS https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
        python /tmp/get-pip.py --quiet || {
            log_warning "Failed to bootstrap pip"
            SKIP_PYTHON=true
        }
        rm -f /tmp/get-pip.py
    fi
fi

if [[ "${SKIP_PYTHON}" != true ]]; then
    # Upgrade pip and setuptools in virtual environment
    # PEP 660 editable installs require pip >= 21.3 and setuptools >= 64.0
    log_info "Upgrading pip and setuptools..."
    python -m pip install --upgrade pip setuptools wheel --quiet --timeout=120 --retries=5 || {
        log_warning "Failed to upgrade pip/setuptools, continuing with existing version..."
    }

    # Install OpenMC Python API in development mode
    log_info "Installing OpenMC Python package in development mode..."
    PYTHON_INSTALL_SUCCESS=false
    if python -m pip install -e . --timeout=120 --retries=5 2>&1; then
        PYTHON_INSTALL_SUCCESS=true
    else
        log_warning "Editable install failed (requires pip >= 21.3, setuptools >= 64.0)"
        log_info "Falling back to regular install..."
        if python -m pip install . --timeout=120 --retries=5 2>&1; then
            PYTHON_INSTALL_SUCCESS=true
        else
            log_warning "Python package install failed."
            log_warning "This may be due to Python version requirements (requires Python >= 3.11)"
            log_warning "OpenMC binary is still available - Python bindings will not work."
            PYTHON_VERSION=$(python3 --version 2>&1 || echo "unknown")
            log_warning "Your Python version: ${PYTHON_VERSION}"
        fi
    fi

    if [[ "${PYTHON_INSTALL_SUCCESS}" == true ]]; then
        log_success "Python virtual environment setup complete"
        log_success "OpenMC Python bindings installed"
    else
        log_warning "Continuing without Python bindings..."
    fi
else
    log_warning "Skipping Python setup due to earlier errors"
fi

################################################################################
# Set up environment
################################################################################

log_info "Configuring environment..."

# Create environment setup script with absolute paths
ENV_SCRIPT="${SCRIPT_DIR}/openmc_env.sh"
cat > "${ENV_SCRIPT}" << EOF
#!/bin/bash
# OpenMC environment setup script
# Source this file to set up the OpenMC environment:
#   source openmc_env.sh

# Get the directory where this script is located
SCRIPT_DIR="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" && pwd)"

# Activate Python virtual environment
if [[ -d "\${SCRIPT_DIR}/.env" ]]; then
    source "\${SCRIPT_DIR}/.env/bin/activate"
    echo "Python virtual environment activated"
else
    echo "Warning: Virtual environment not found at \${SCRIPT_DIR}/.env"
fi

# Add OpenMC binary to PATH (using absolute path)
export PATH="${INSTALL_PREFIX}/bin:\${PATH}"

# Set cross section data path (using absolute path)
export OPENMC_CROSS_SECTIONS="${XS_DATA_DIR}/cross_sections.xml"
$(if [[ "${WITH_FISSION_LIB}" == true ]]; then
cat <<EOFI

# FREYA / Fission Library was linked into this OpenMC build.
# OPENMC_USE_FISSION_LIB lets the validation tests detect that.
# FREYA_DATA_PATH overrides the compile-time data path if needed.
export OPENMC_USE_FISSION_LIB=1
export FREYA_DATA_PATH="${FISSION_LIB_ROOT}/data_freya"
EOFI
fi)

echo "OpenMC environment configured:"
echo "  OpenMC executable: \$(which openmc 2>/dev/null || echo 'not found in PATH')"
echo "  Cross sections: \${OPENMC_CROSS_SECTIONS}"
echo "  Python: \$(which python)"
if [[ -n "\${OPENMC_USE_FISSION_LIB:-}" ]]; then
    echo "  FREYA: enabled (data: \${FREYA_DATA_PATH})"
fi
EOF

chmod +x "${ENV_SCRIPT}"

log_success "Environment script created: ${ENV_SCRIPT}"

################################################################################
# Verify installation
################################################################################

log_info "Verifying installation..."

# Check if openmc binary exists
if command -v openmc &> /dev/null; then
    OPENMC_VERSION=$(openmc --version 2>&1 || echo "unknown")
    log_success "OpenMC executable found: $(which openmc)"
    log_info "Version: ${OPENMC_VERSION}"
else
    log_warning "OpenMC executable not found in PATH"
fi

# Check Python module (should still be in activated venv)
if python -c "import openmc; print(f'OpenMC Python API version: {openmc.__version__}')" 2>/dev/null; then
    log_success "OpenMC Python module imported successfully"
else
    log_error "Failed to import OpenMC Python module"
    exit 1
fi

################################################################################
# Print summary
################################################################################

echo ""
echo "================================================================================"
log_success "OpenMC installation completed successfully!"
echo "================================================================================"
echo ""
echo "Installation summary:"
echo "  - OpenMC installed to: ${INSTALL_PREFIX}"
echo "  - Cross section data: ${XS_DATA_DIR}"
echo "  - Python virtual environment: ${VENV_DIR}"
echo "  - Build type: ${BUILD_TYPE}"
echo "  - MPI support: $([ "$WITH_MPI" == true ] && echo "Enabled" || echo "Disabled")"
echo "  - FREYA / Fission Library: $([ "$WITH_FISSION_LIB" == true ] && echo "Enabled (libFission: ${FISSION_LIB_FOUND})" || echo "Disabled")"
echo ""
echo "To use OpenMC in a new terminal, run:"
echo "  cd ${SCRIPT_DIR}"
echo "  source openmc_env.sh"
echo ""
echo "This will:"
echo "  - Activate the Python virtual environment"
echo "  - Add OpenMC binary to PATH"
echo "  - Set OPENMC_CROSS_SECTIONS environment variable"
echo ""
echo "To test the installation, try running one of the examples:"
echo "  source openmc_env.sh"
echo "  cd examples"
echo "  python kinetics_benchmark_problem1.py"
echo ""
echo "================================================================================"
