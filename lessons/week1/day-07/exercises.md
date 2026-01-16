# Day 7: Debugging, Profiling, and Python Capstone - Exercises

## Python Capstone: Statistical Analysis Pipeline

**Time Estimate**: 90-120 minutes

### Overview

Build a complete statistical analysis pipeline that demonstrates all Week 1 skills. You will implement a module for analyzing experimental data, including data loading, cleaning, statistical analysis, and reporting.

### Specification

Create a package `statpipe` with the following structure:

```
statpipe/
├── __init__.py
├── io.py           # Data loading and saving
├── clean.py        # Data cleaning and validation
├── stats.py        # Statistical computations
├── report.py       # Report generation
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_io.py
    ├── test_clean.py
    ├── test_stats.py
    └── test_report.py
```

### Required Functions

#### io.py
```python
def load_experiment_data(
    path: Path,
    logger: logging.Logger | None = None
) -> pd.DataFrame:
    """Load experimental data from CSV with validation."""

def save_results(
    results: dict,
    path: Path,
    logger: logging.Logger | None = None
) -> None:
    """Save analysis results to JSON."""
```

#### clean.py
```python
def validate_data(df: pd.DataFrame) -> list[str]:
    """Return list of validation warnings."""

def remove_outliers(
    df: pd.DataFrame,
    column: str,
    n_std: float = 3.0
) -> pd.DataFrame:
    """Remove outliers beyond n standard deviations."""

def impute_missing(
    df: pd.DataFrame,
    strategy: str = "mean"
) -> pd.DataFrame:
    """Impute missing values."""
```

#### stats.py
```python
def compute_summary_stats(df: pd.DataFrame, column: str) -> dict:
    """Compute mean, std, median, IQR."""

def bootstrap_ci(
    data: np.ndarray,
    statistic: Callable,
    n_bootstrap: int = 1000,
    confidence: float = 0.95,
    rng: np.random.Generator | None = None
) -> tuple[float, float]:
    """Compute bootstrap confidence interval."""

def compare_groups(
    group1: np.ndarray,
    group2: np.ndarray,
    rng: np.random.Generator | None = None
) -> dict:
    """Compare two groups with t-test and effect size."""
```

#### report.py
```python
def generate_report(
    data: pd.DataFrame,
    analysis_results: dict,
    output_path: Path
) -> None:
    """Generate markdown report."""
```

### Requirements Checklist

- [ ] All functions have type hints
- [ ] All functions have docstrings (NumPy or Google style)
- [ ] Context managers used for all file operations
- [ ] No chained indexing in Pandas code
- [ ] All array operations vectorized (no Python loops over data)
- [ ] All random operations accept `rng` parameter
- [ ] Logging used throughout (no print statements)
- [ ] Tests achieve >80% coverage
- [ ] Tests use fixtures and parametrize
- [ ] Memory-safe: no unintended mutations

### Sample Usage

```python
import logging
from pathlib import Path
import numpy as np
from statpipe import io, clean, stats, report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

rng = np.random.default_rng(42)

# Load and clean data
data = io.load_experiment_data(Path("experiment.csv"), logger)
warnings = clean.validate_data(data)
data = clean.remove_outliers(data, "response")
data = clean.impute_missing(data)

# Analyze
summary = stats.compute_summary_stats(data, "response")
ci = stats.bootstrap_ci(data["response"].values, np.mean, rng=rng)
comparison = stats.compare_groups(
    data[data["condition"] == "A"]["response"].values,
    data[data["condition"] == "B"]["response"].values,
    rng=rng
)

# Report
results = {"summary": summary, "confidence_interval": ci, "comparison": comparison}
io.save_results(results, Path("results.json"), logger)
report.generate_report(data, results, Path("report.md"))
```

### Rubric

| Dimension | 0 | 1 | 2 |
|-----------|---|---|---|
| **Code Quality** | Missing type hints/docstrings | Partial coverage | Complete and consistent |
| **Functionality** | Major bugs | Minor issues | All features work |
| **Best Practices** | Multiple violations | Minor violations | All practices followed |
| **Testing** | < 50% coverage | 50-80% coverage | > 80% coverage |

### Submission

1. Complete implementation in `lessons/week1/day-07/python/statpipe/`
2. Run tests: `pytest lessons/week1/day-07/python/tests/ -v --cov=statpipe`
3. Verify coverage > 80%
4. Profile key functions and document any optimizations made

---

## Debugging Exercise (Warmup)

Before starting the capstone, debug this function:

```python
def compute_weighted_mean(values, weights):
    """Compute weighted mean. Has 3 bugs."""
    total = 0
    weight_sum = 0
    for i in range(len(values)):
        total = values[i] * weights[i]  # Bug 1
        weight_sum += weights[i]
    return total / weight_sum  # Bug 2 (also: what if weight_sum is 0?)

# Bug 3: What if values and weights have different lengths?
```
