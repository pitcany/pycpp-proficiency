# Day 3: Broadcasting and Vectorization - Exercises

## Foundational Exercises

### Exercise 3.1: Normalize by Row and Column

**Objective**: Use broadcasting to normalize a matrix.

```python
import numpy as np

def normalize_rows(X: np.ndarray) -> np.ndarray:
    """Normalize each row to sum to 1."""
    # TODO: Implement using broadcasting (no loops)
    pass

def normalize_columns(X: np.ndarray) -> np.ndarray:
    """Normalize each column to have zero mean and unit variance."""
    # TODO: Implement using broadcasting (no loops)
    pass

# Test
X = np.array([[1., 2., 3.],
              [4., 5., 6.]])

row_normalized = normalize_rows(X)
# Each row should sum to 1

col_normalized = normalize_columns(X)
# Each column should have mean 0, std 1
```

---

### Exercise 3.2: Vectorize Sigmoid Function

**Objective**: Implement sigmoid without Python loops.

```python
def sigmoid_loop(x: np.ndarray) -> np.ndarray:
    """Sigmoid using explicit loop (slow)."""
    result = np.zeros_like(x)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            result[i, j] = 1 / (1 + np.exp(-x[i, j]))
    return result

def sigmoid_vectorized(x: np.ndarray) -> np.ndarray:
    """Sigmoid using vectorization (fast)."""
    # TODO: Implement
    pass

# Benchmark both versions
import time
X = np.random.randn(1000, 1000)

start = time.time()
sigmoid_loop(X)
print(f"Loop: {time.time() - start:.3f}s")

start = time.time()
sigmoid_vectorized(X)
print(f"Vectorized: {time.time() - start:.3f}s")
```

---

## Proficiency Exercises

### Exercise 3.3: Pairwise Differences

**Objective**: Compute all pairwise differences using broadcasting.

```python
def pairwise_differences(x: np.ndarray) -> np.ndarray:
    """
    Compute pairwise differences.

    Args:
        x: 1D array of shape (n,)

    Returns:
        2D array D of shape (n, n) where D[i,j] = x[i] - x[j]
    """
    # TODO: Implement using broadcasting (one line!)
    pass
```

---

### Exercise 3.4: Softmax Along Axis

**Objective**: Implement stable softmax along a specified axis.

```python
def softmax(X: np.ndarray, axis: int = -1) -> np.ndarray:
    """
    Compute softmax along the specified axis.

    Uses the log-sum-exp trick for numerical stability.
    """
    # TODO: Implement with broadcasting
    # Hint: Use np.max and np.sum with keepdims=True
    pass

# Test
X = np.array([[1., 2., 3.],
              [1., 2., 1000.]])  # Second row has large values

result = softmax(X, axis=1)
# Each row should sum to 1, no overflow
assert np.allclose(result.sum(axis=1), 1.0)
```

---

### Exercise 3.5: Gaussian PDF

**Objective**: Compute Gaussian PDF for multiple points and parameters.

```python
def gaussian_pdf(x: np.ndarray, mu: np.ndarray, sigma: np.ndarray) -> np.ndarray:
    """
    Compute Gaussian PDF.

    Args:
        x: Data points, shape (n,)
        mu: Means, shape (k,)
        sigma: Standard deviations, shape (k,)

    Returns:
        PDF values, shape (n, k) where result[i, j] = N(x[i] | mu[j], sigma[j])
    """
    # TODO: Implement using broadcasting
    pass

# Test
x = np.array([0., 1., 2.])
mu = np.array([0., 1.])
sigma = np.array([1., 0.5])

result = gaussian_pdf(x, mu, sigma)  # Shape (3, 2)
```

---

## Mastery Exercises

### Exercise 3.6: K-Means Assignment Step

**Objective**: Vectorize the cluster assignment in k-means.

```python
def assign_clusters(X: np.ndarray, centroids: np.ndarray) -> np.ndarray:
    """
    Assign each point to the nearest centroid.

    Args:
        X: Data points, shape (n, d)
        centroids: Cluster centers, shape (k, d)

    Returns:
        Cluster assignments, shape (n,) with values in [0, k-1]
    """
    # TODO: Implement without loops
    # Hint: Compute all pairwise distances, then argmin
    pass
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| No loops | Uses loops | Partial vectorization | Fully vectorized |
| Correctness | Wrong results | Minor errors | Correct |
| Broadcasting | Misunderstands rules | Basic usage | Expert usage |
| Performance | Slow | Acceptable | Optimal |
