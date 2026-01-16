# Day 1: Functions, Modules, and Idiomatic Python - Exercises

## Foundational Exercises

### Exercise 1.1: Refactor Function

**Objective**: Refactor a poorly-written function to follow best practices.

**Before** (in `python/before_refactor.py`):
```python
def calc(d, c=None):
    # compute stuff
    if c == None:
        c = []
    r = 0
    for i in range(len(d)):
        r = r + d[i]
    c.append(r)
    return r
```

**Task**: Refactor to include:
1. Descriptive function and parameter names
2. Type hints
3. Docstring
4. Fix the mutable default argument bug
5. Use pythonic iteration

**Expected output** (in `python/after_refactor.py`):
```python
def compute_sum(data: list[float], results: list[float] | None = None) -> float:
    """
    Compute the sum of a list of numbers.

    Args:
        data: List of numbers to sum.
        results: Optional list to append the result to.

    Returns:
        The sum of all numbers in data.
    """
    if results is None:
        results = []
    total = sum(data)
    results.append(total)
    return total
```

---

### Exercise 1.2: Module Design

**Objective**: Organize a flat script into a proper module structure.

**Task**: Given a script with multiple functions, create:
```
python/
├── __init__.py
├── stats.py       # Statistical functions
├── io.py          # File I/O utilities
└── utils.py       # Helper functions
```

**Requirements**:
1. Each module should have a module-level docstring
2. Use `__all__` to control public API
3. Create a clean `__init__.py` that exposes the public interface
4. Demonstrate relative imports

**Starter code** (in `python/flat_script.py`):
```python
import numpy as np

def load_data(path):
    return np.loadtxt(path)

def compute_mean(arr):
    return np.mean(arr)

def compute_std(arr):
    return np.std(arr)

def save_results(path, results):
    np.savetxt(path, results)

def normalize(arr):
    return (arr - compute_mean(arr)) / compute_std(arr)
```

---

## Proficiency Exercises

### Exercise 1.3: Custom Context Manager

**Objective**: Implement a context manager for timing code blocks.

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name: str = "Block"):
    """
    Context manager that times the execution of a block.

    Usage:
        with timer("My operation"):
            expensive_computation()

    Prints: "My operation took 1.234s"
    """
    # TODO: Implement
    pass
```

---

### Exercise 1.4: Generator for Large Files

**Objective**: Create a generator that processes large CSV files line by line.

```python
from typing import Iterator

def read_csv_rows(path: str) -> Iterator[dict[str, str]]:
    """
    Lazily read rows from a CSV file.

    Yields:
        Each row as a dictionary mapping column names to values.
    """
    # TODO: Implement using generators
    pass
```

---

## Mastery Exercises

### Exercise 1.5: Decorator for Validation

**Objective**: Write a decorator that validates function arguments.

```python
from functools import wraps
from typing import Callable, TypeVar

F = TypeVar('F', bound=Callable)

def validate_positive(*arg_names: str) -> Callable[[F], F]:
    """
    Decorator that validates specified arguments are positive.

    Usage:
        @validate_positive('x', 'y')
        def compute(x: float, y: float) -> float:
            return x + y

        compute(-1, 2)  # Raises ValueError
    """
    # TODO: Implement
    pass
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Type hints | Missing | Partial | Complete and correct |
| Docstrings | Missing | Present but incomplete | Full with examples |
| Code organization | Disorganized | Mostly clean | Clean with proper modules |
| Pythonic style | Uses non-pythonic patterns | Mostly pythonic | Fully idiomatic |
