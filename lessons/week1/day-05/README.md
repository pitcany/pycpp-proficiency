# Day 5: Testable, Reusable Code

**Language**: Python
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/5de7edf40e5241dfbad236f5bbd4717f)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Design functions with single responsibilities
- [ ] Write unit tests with pytest
- [ ] Use fixtures and parametrize tests
- [ ] Organize code into packages
- [ ] Apply test-driven development (TDD) basics

## Sections

### Function Design Principles

Writing testable functions:
- Single responsibility principle
- Pure functions (no side effects)
- Dependency injection
- Separation of concerns

### Unit Testing with pytest

Testing fundamentals:
```python
# test_stats.py
import pytest
from stats import compute_mean

def test_compute_mean_basic():
    assert compute_mean([1, 2, 3]) == 2.0

def test_compute_mean_empty():
    with pytest.raises(ValueError):
        compute_mean([])
```

### Fixtures and Parametrize

Reusable test setup and data-driven tests:
```python
@pytest.fixture
def sample_data():
    return np.array([1, 2, 3, 4, 5])

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], 2.0),
    ([0, 0, 0], 0.0),
    ([1], 1.0),
])
def test_mean_parametrized(input, expected):
    assert compute_mean(input) == expected
```

### Package Organization

Project structure for reusability:
```
mypackage/
├── __init__.py
├── core/
│   ├── __init__.py
│   └── algorithms.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── tests/
    ├── __init__.py
    ├── test_algorithms.py
    └── conftest.py  # Shared fixtures
```

### Test-Driven Development (TDD)

Red-Green-Refactor cycle:
1. Write a failing test (Red)
2. Write minimal code to pass (Green)
3. Improve code quality (Refactor)

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Pure functions are easier to test
2. Use fixtures for common test setup
3. Parametrize tests for multiple inputs
4. TDD leads to better design

## Next Steps

Proceed to [Day 6: Reproducibility, Randomness, and State](../day-06/README.md).
