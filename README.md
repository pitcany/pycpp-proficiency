# 2-Week Python & C++ Proficiency for Statisticians and Data Scientists

**Version**: 1.0.0-beta | **Last Updated**: January 2, 2026

A comprehensive curriculum for working proficiency in statistical computing: implementing numerically stable algorithms in Python (NumPy/pandas ecosystem) and foundational C++ skills for performance-critical numerical code.

## Prerequisites

This curriculum assumes fluency in:
- Probability and statistics
- Linear algebra
- Optimization
- Basic Python and C++ syntax

## Quick Start

### macOS Setup

```bash
# Run the bootstrap script
./scripts/bootstrap_macos.sh

# Activate the virtual environment
source .venv/bin/activate

# Verify setup
make check
```

### Manual Setup

```bash
# Python environment (using uv)
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"

# C++ build
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

## Course Structure

```
Week 0: Foundations
├── Day 0: Environment Setup
└── Algorithmic Thinking for Statistical Code

Week 1: Python (Days 1-7)
├── Day 1: Functions, Modules, and Idiomatic Python
├── Day 2: Memory Model, Views, and Copies
├── Day 3: Broadcasting and Vectorization
├── Day 4: Pandas Pitfalls and Alternatives
├── Day 5: Testable, Reusable Code
├── Day 6: Reproducibility, Randomness, and State
└── Day 7: Debugging, Profiling, and Python Capstone

Week 2: C++ (Days 8-14)
├── Day 8: References, Pointers, and Ownership
├── Day 9: Smart Pointers and Ownership Semantics
├── Day 10: RAII, Move Semantics, and Destructors
├── Day 11: STL Containers, Algorithms, and Iterators
├── Day 12: Numerical Stability and Floating-Point
├── Day 13: Performance Reasoning and Optimization
└── Day 14: C++ Capstone and Cross-Language Integration

Week 3: Optional Extensions (Days 15-20)
├── Day 15: Advanced Python Engineering
├── Day 16: Profiling and Performance Tuning
├── Day 17: Python ↔ C++ Boundaries
├── Day 18: Numerical Robustness and Stress Testing
├── Day 19: C++ Numerical Patterns and RAII
└── Day 20: Compilation and Microbenchmarking
```

## Repository Layout

```
pycpp-proficiency/
├── README.md                 # This file
├── pyproject.toml            # Python package configuration
├── CMakeLists.txt            # C++ build configuration
├── Makefile                  # Development workflow targets
├── .gitignore
├── .env.example
│
├── course_manifest/
│   └── manifest.json         # Course structure from Notion
│
├── lessons/
│   ├── foundations/
│   ├── week1/
│   ├── week2/
│   └── week3/
│
├── src/
│   ├── python_lib/           # Shared Python utilities
│   └── cpp_lib/              # Shared C++ utilities
│
├── scripts/
│   ├── bootstrap_macos.sh    # macOS setup script
│   ├── sync_from_notion.py   # Re-sync content from Notion
│   ├── generate_from_manifest.py  # Generate lesson structure
│   └── check.sh              # Verification script
│
├── benchmarks/               # Performance benchmarks
├── notebooks/                # Jupyter notebooks
└── tests/
    ├── python/
    └── cpp/
```

## Proficiency Standards

To claim proficiency from this curriculum:

1. **Exercise Performance**
   - Score ≥1.5/2.0 average across all Foundational exercises
   - Complete ≥75% of Proficiency exercises with ≥1.5/2.0

2. **Capstone Performance**
   - Score ≥1.5/2.0 on EACH dimension of both capstone rubrics

3. **Oral Defense Readiness**
   - Answer ≥80% of oral defense questions at "strong answer" level

4. **Time Investment**
   - Expect 50-60 hours total (6-8 hours/day × 2 weeks)

## Development Commands

```bash
# Bootstrap the environment
make bootstrap

# Format code
make fmt

# Run linters
make lint

# Run all tests
make test

# Sync from Notion (requires API access)
make sync-notion

# Regenerate from manifest
make gen-from-manifest

# Run a specific lesson
make run-lesson WEEK=week1 LESSON=day-01

# Build C++ targets
make build-cpp

# Run C++ tests
make test-cpp

# Run C++ demo
make run-cpp-demo
```

## Adding New Lessons

1. Update the course in Notion
2. Run `make sync-notion` to update the manifest
3. Run `make gen-from-manifest` to regenerate lesson structure
4. Add exercise code to the appropriate `python/` or `cpp/` directories

## License

This curriculum is for educational purposes. See LICENSE for details.

---

*Source: Notion course "2-Week Python & C++ Proficiency for Statisticians and Data Scientists"*
