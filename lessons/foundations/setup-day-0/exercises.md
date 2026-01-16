# Setup (Day 0) - Exercises

This lesson focuses on environment setup. There are no coding exercises, but you should complete the following verification tasks.

## Verification Checklist

### Python Environment

- [ ] Python 3.10+ is installed and accessible
- [ ] Virtual environment created with `uv venv`
- [ ] All dependencies installed with `uv pip install -e ".[dev]"`
- [ ] `pytest` runs without errors
- [ ] `ruff check` runs without errors

### C++ Environment

- [ ] C++ compiler (g++ 9+ or clang 12+) is installed
- [ ] CMake 3.16+ is installed
- [ ] Can compile a simple C++17 program
- [ ] AddressSanitizer works: `g++ -fsanitize=address -g test.cpp`
- [ ] UndefinedBehaviorSanitizer works: `g++ -fsanitize=undefined -g test.cpp`

### Verification Script

Run the full verification:

```bash
./scripts/check.sh
```

Expected output:
```
[OK] Python 3.x.x
[OK] C++ compiler: g++ x.x.x
[OK] CMake x.x.x
[OK] Virtual environment active
[OK] All Python dependencies installed
[OK] Sanitizers working
```

## Troubleshooting

If any checks fail, consult the README for troubleshooting steps.
