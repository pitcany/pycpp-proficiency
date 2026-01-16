# Day 5: Testable, Reusable Code - Exercises

## Foundational Exercises

### Exercise 5.1: Write Tests

**Objective**: Write comprehensive tests for given functions.

```python
# stats.py
import numpy as np

def compute_variance(x: np.ndarray, ddof: int = 1) -> float:
    """Compute sample variance with specified degrees of freedom."""
    n = len(x)
    if n < ddof + 1:
        raise ValueError(f"Need at least {ddof + 1} samples")
    mean = np.mean(x)
    return np.sum((x - mean) ** 2) / (n - ddof)

def z_score(x: np.ndarray) -> np.ndarray:
    """Standardize array to zero mean and unit variance."""
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    if std == 0:
        raise ValueError("Cannot standardize constant array")
    return (x - mean) / std
```

**Task**: Write tests in `test_stats.py`:
1. Test `compute_variance` with known values
2. Test edge cases (single element, all same values)
3. Test error conditions
4. Use `@pytest.mark.parametrize` for multiple test cases
5. Test `z_score` similarly

---

### Exercise 5.2: Refactor for Testability

**Objective**: Refactor untestable code to be testable.

```python
# Bad: Hard to test due to hardcoded dependencies
import pandas as pd
from datetime import datetime

def generate_report():
    # Hardcoded file path
    data = pd.read_csv('/data/sales.csv')

    # Uses current time
    today = datetime.now()
    data = data[data['date'] < today]

    # Hardcoded output
    summary = data.groupby('product').sum()
    summary.to_csv('/reports/summary.csv')

    return summary
```

**Task**: Refactor to:
1. Accept file paths as parameters
2. Accept date as a parameter
3. Return data instead of writing to file
4. Write tests for the refactored function

---

## Proficiency Exercises

### Exercise 5.3: Fixtures and Conftest

**Objective**: Create reusable fixtures for statistical tests.

Create `conftest.py`:
```python
import pytest
import numpy as np

@pytest.fixture
def rng():
    """Reproducible random number generator."""
    return np.random.default_rng(42)

@pytest.fixture
def normal_sample(rng):
    """Standard normal sample for testing."""
    return rng.standard_normal(1000)

@pytest.fixture
def small_sample():
    """Small sample for edge case testing."""
    return np.array([1.0, 2.0, 3.0])

# TODO: Add more fixtures
```

---

### Exercise 5.4: TDD Exercise

**Objective**: Implement a function using TDD.

**Specification**: Implement `bootstrap_mean_ci(x, n_bootstrap, confidence, rng)`

Write tests FIRST, then implement:

```python
# test_bootstrap.py
import pytest
import numpy as np

def test_bootstrap_mean_ci_returns_tuple():
    """Should return (lower, upper) tuple."""
    pass

def test_bootstrap_mean_ci_contains_true_mean():
    """CI should contain true mean for large samples."""
    pass

def test_bootstrap_mean_ci_confidence_level():
    """Higher confidence should give wider intervals."""
    pass

def test_bootstrap_mean_ci_reproducible():
    """Same rng seed should give same result."""
    pass

# After writing tests, implement:
# bootstrap.py
def bootstrap_mean_ci(
    x: np.ndarray,
    n_bootstrap: int = 1000,
    confidence: float = 0.95,
    rng: np.random.Generator | None = None
) -> tuple[float, float]:
    """
    Compute bootstrap confidence interval for the mean.

    Args:
        x: Sample data
        n_bootstrap: Number of bootstrap samples
        confidence: Confidence level (0 < confidence < 1)
        rng: Random number generator for reproducibility

    Returns:
        Tuple of (lower_bound, upper_bound)
    """
    pass
```

---

## Mastery Exercises

### Exercise 5.5: Property-Based Testing

**Objective**: Use Hypothesis for property-based testing.

```python
from hypothesis import given, strategies as st
import numpy as np

# Test that variance is always non-negative
@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=2))
def test_variance_non_negative(data):
    x = np.array(data)
    var = compute_variance(x)
    assert var >= 0

# TODO: Add more property-based tests
# - z_score should have mean ~0 and std ~1
# - bootstrap CI lower <= upper
# - variance of constant array is 0
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Test coverage | < 50% | 50-80% | > 80% |
| Edge cases | Not tested | Some tested | Comprehensive |
| Fixtures | Not used | Basic usage | Well-organized |
| TDD adherence | Tests after | Mixed | Tests first |
