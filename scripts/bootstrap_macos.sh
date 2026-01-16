#!/bin/bash
# Bootstrap script for macOS development environment
set -euo pipefail

echo "=== pycpp-proficiency Bootstrap (macOS) ==="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

check_command() {
    if command -v "$1" &> /dev/null; then
        echo -e "${GREEN}[OK]${NC} $1 found"
        return 0
    else
        echo -e "${RED}[MISSING]${NC} $1 not found"
        return 1
    fi
}

# Check prerequisites
echo "Checking prerequisites..."
echo ""

# Python
if check_command python3; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    echo "     Python version: $PYTHON_VERSION"
fi

# uv (Python package manager)
if ! check_command uv; then
    echo -e "${YELLOW}Installing uv...${NC}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# C++ compiler
if check_command clang++; then
    CLANG_VERSION=$(clang++ --version 2>&1 | head -1)
    echo "     $CLANG_VERSION"
elif check_command g++; then
    GCC_VERSION=$(g++ --version 2>&1 | head -1)
    echo "     $GCC_VERSION"
else
    echo -e "${RED}No C++ compiler found. Install Xcode Command Line Tools:${NC}"
    echo "     xcode-select --install"
    exit 1
fi

# CMake
if ! check_command cmake; then
    echo -e "${YELLOW}Installing cmake via Homebrew...${NC}"
    if check_command brew; then
        brew install cmake
    else
        echo -e "${RED}Please install CMake: https://cmake.org/download/${NC}"
        exit 1
    fi
fi

echo ""
echo "Setting up Python environment..."
echo ""

# Create virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv
fi

# Activate and install
echo "Installing Python dependencies..."
source .venv/bin/activate
uv pip install -e ".[dev]"

echo ""
echo "Setting up C++ build..."
echo ""

# Create build directory
mkdir -p build
cd build

# Configure CMake
echo "Configuring CMake..."
cmake .. -DCMAKE_BUILD_TYPE=Release

# Build
echo "Building C++ components..."
cmake --build . --parallel

cd ..

echo ""
echo "=== Bootstrap Complete ==="
echo ""
echo "To activate the environment:"
echo "    source .venv/bin/activate"
echo ""
echo "To verify setup:"
echo "    make check"
echo ""
echo "To run tests:"
echo "    make test"
