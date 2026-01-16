# Day 2: Memory Model, Views, and Copies - Exercises

## Foundational Exercises

### Exercise 2.1: Debug the Mutation

**Objective**: Identify and fix unintended mutation bugs.

**Bug 1**: List mutation
```python
def append_sum(data: list[list[int]]) -> list[list[int]]:
    """Append the sum to each sublist."""
    result = data  # Bug: creates a reference, not a copy
    for sublist in result:
        sublist.append(sum(sublist))
    return result

# Test
original = [[1, 2], [3, 4]]
modified = append_sum(original)
print(original)  # Unexpectedly modified!
```

**Task**: Fix the function so `original` is not modified.

---

**Bug 2**: NumPy view mutation
```python
import numpy as np

def normalize_columns(X: np.ndarray) -> np.ndarray:
    """Normalize each column to have zero mean."""
    result = X[:, :]  # Bug: this is a view!
    for j in range(X.shape[1]):
        result[:, j] -= result[:, j].mean()
    return result

# Test
X = np.array([[1., 2.], [3., 4.]])
normalized = normalize_columns(X)
print(X)  # Unexpectedly modified!
```

**Task**: Fix the function so `X` is not modified.

---

### Exercise 2.2: NumPy View Detective

**Objective**: Predict whether each operation returns a view or a copy.

For each operation, predict (view/copy) then verify:

```python
import numpy as np

X = np.arange(12).reshape(3, 4)

# 1. Basic slicing
a = X[0]                    # View or copy?
b = X[0, :]                 # View or copy?
c = X[:, 0]                 # View or copy?
d = X[::2]                  # View or copy?

# 2. Advanced indexing
e = X[[0, 1]]               # View or copy?
f = X[:, [0, 2]]            # View or copy?
g = X[X > 5]                # View or copy?

# 3. Operations
h = X.T                     # View or copy?
i = X.ravel()               # View or copy?
j = X.flatten()             # View or copy?
k = X.reshape(4, 3)         # View or copy?
l = X + 0                   # View or copy?
```

**Verification code**:
```python
def is_view(arr, X):
    return np.shares_memory(arr, X)
```

---

## Proficiency Exercises

### Exercise 2.3: Safe Matrix Operations

**Objective**: Write functions that never modify input arrays.

```python
import numpy as np

def safe_row_normalize(X: np.ndarray) -> np.ndarray:
    """
    Normalize each row to sum to 1.

    Args:
        X: 2D array of shape (n, m)

    Returns:
        New array where each row sums to 1.
        Original X is never modified.
    """
    # TODO: Implement safely
    pass

def safe_center(X: np.ndarray) -> np.ndarray:
    """
    Center data to have zero mean per column.

    Returns a new array; original X is not modified.
    """
    # TODO: Implement safely
    pass
```

---

### Exercise 2.4: Memory-Efficient Processing

**Objective**: Process data in-place when memory efficiency matters.

```python
def inplace_standardize(X: np.ndarray) -> None:
    """
    Standardize array in-place (zero mean, unit variance per column).

    Modifies X directly. No return value.
    """
    # TODO: Implement in-place
    pass
```

---

## Mastery Exercises

### Exercise 2.5: Deep vs Shallow Copy Analysis

**Objective**: Analyze and fix a complex nested structure bug.

```python
from copy import copy, deepcopy

class DataContainer:
    def __init__(self, data: list, metadata: dict):
        self.data = data
        self.metadata = metadata

def process_containers(containers: list[DataContainer]) -> list[DataContainer]:
    """
    Process each container, modifying data but preserving originals.

    This function has bugs related to shallow vs deep copying.
    Find and fix them.
    """
    result = copy(containers)  # Is this enough?
    for container in result:
        container.data = [x * 2 for x in container.data]
        container.metadata['processed'] = True
    return result
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| View/copy identification | Many errors | Minor errors | All correct |
| Mutation prevention | Bugs present | Mostly safe | Fully safe |
| Memory understanding | Confused | Basic understanding | Deep understanding |
| Code correctness | Doesn't work | Works with issues | Fully correct |
