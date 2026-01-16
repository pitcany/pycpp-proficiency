#!/bin/bash
# Verify development environment is correctly set up
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ERRORS=0

check() {
    local name="$1"
    local cmd="$2"

    if eval "$cmd" &> /dev/null; then
        echo -e "${GREEN}[OK]${NC} $name"
    else
        echo -e "${RED}[FAIL]${NC} $name"
        ERRORS=$((ERRORS + 1))
    fi
}

echo "=== Environment Check ==="
echo ""

# Python checks
echo "Python:"
check "Python 3.10+" "python3 -c 'import sys; assert sys.version_info >= (3, 10)'"
check "Virtual environment active" "[ -n \"\${VIRTUAL_ENV:-}\" ]"
check "NumPy installed" "python3 -c 'import numpy'"
check "Pandas installed" "python3 -c 'import pandas'"
check "Pytest installed" "python3 -c 'import pytest'"
check "Python lib importable" "python3 -c 'import python_lib'"

echo ""
echo "C++:"
check "C++ compiler (clang++ or g++)" "command -v clang++ || command -v g++"
check "CMake 3.16+" "cmake --version | head -1 | grep -E '3\.(1[6-9]|[2-9][0-9])'"
check "Build directory exists" "[ -d build ]"
check "Demo executable built" "[ -f build/demo ]"

echo ""
echo "Tools:"
check "Ruff (linter)" "command -v ruff"
check "Black (formatter)" "command -v black"

echo ""
echo "Sanitizers:"
if command -v clang++ &> /dev/null; then
    check "AddressSanitizer" "echo 'int main(){}' | clang++ -fsanitize=address -x c++ - -o /dev/null 2>/dev/null"
elif command -v g++ &> /dev/null; then
    check "AddressSanitizer" "echo 'int main(){}' | g++ -fsanitize=address -x c++ - -o /dev/null 2>/dev/null"
fi

echo ""
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}All checks passed!${NC}"
    exit 0
else
    echo -e "${RED}$ERRORS check(s) failed${NC}"
    exit 1
fi
