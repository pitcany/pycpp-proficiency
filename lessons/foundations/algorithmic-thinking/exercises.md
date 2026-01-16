# Algorithmic Thinking - Exercises

## Foundational Exercises

### F1: Log-Sum-Exp Stable Computation

**Objective**: Implement a numerically stable version of log-sum-exp.

**Problem**: Given a vector of log-probabilities, compute `log(sum(exp(x)))` without overflow/underflow.

```python
def log_sum_exp(x: np.ndarray) -> float:
    """Compute log(sum(exp(x))) in a numerically stable way."""
    # TODO: Implement
    pass
```

**Test cases**:
```python
# Should not overflow
assert np.isclose(log_sum_exp(np.array([1000, 1000, 1000])), 1000 + np.log(3))

# Should not underflow
assert np.isclose(log_sum_exp(np.array([-1000, -1000, -1000])), -1000 + np.log(3))
```

---

### F2: Running Mean and Variance (Welford)

**Objective**: Implement Welford's online algorithm for computing mean and variance in a single pass.

```python
class WelfordAccumulator:
    """Online mean and variance using Welford's algorithm."""

    def __init__(self):
        # TODO: Initialize state
        pass

    def update(self, x: float) -> None:
        """Add a new observation."""
        pass

    @property
    def mean(self) -> float:
        """Return current mean."""
        pass

    @property
    def variance(self) -> float:
        """Return current sample variance."""
        pass
```

---

### F3: Discrete Distribution Sampling

**Objective**: Sample from a discrete distribution given probabilities.

```python
def sample_discrete(probs: np.ndarray, rng: np.random.Generator) -> int:
    """Sample an index according to the given probabilities."""
    # TODO: Implement
    pass
```

---

## Proficiency Exercises

### P1: Pairwise Euclidean Distances Without Loops

**Objective**: Compute pairwise Euclidean distances using only vectorized operations.

```python
def pairwise_distances(X: np.ndarray) -> np.ndarray:
    """
    Compute pairwise Euclidean distances.

    Args:
        X: Array of shape (n_samples, n_features)

    Returns:
        D: Array of shape (n_samples, n_samples) where D[i,j] = ||X[i] - X[j]||
    """
    # TODO: Implement without loops
    pass
```

---

### P2: Reservoir Sampling

**Objective**: Implement reservoir sampling for selecting k items uniformly from a stream.

```python
def reservoir_sample(stream: Iterator[T], k: int, rng: np.random.Generator) -> list[T]:
    """Select k items uniformly at random from a stream of unknown length."""
    # TODO: Implement
    pass
```

---

### P3: Solve Ax=b Without Explicit Inversion

**Objective**: Solve a linear system without computing the matrix inverse.

```python
def solve_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solve Ax = b without computing A^{-1}.

    Use np.linalg.solve or a decomposition method.
    """
    # TODO: Implement
    pass
```

---

## Mastery Exercises

### M1: Kahan Summation

**Objective**: Implement compensated summation to reduce floating-point error.

```python
def kahan_sum(x: np.ndarray) -> float:
    """Sum array elements using Kahan summation."""
    # TODO: Implement
    pass
```

---

### M2: Stable Softmax

**Objective**: Implement numerically stable softmax.

```python
def stable_softmax(x: np.ndarray) -> np.ndarray:
    """Compute softmax in a numerically stable way."""
    # TODO: Implement
    pass
```

---

### M3: Iterative Refinement

**Objective**: Improve the solution to an ill-conditioned linear system using iterative refinement.

```python
def iterative_refinement(A: np.ndarray, b: np.ndarray, max_iter: int = 10) -> np.ndarray:
    """Solve Ax=b with iterative refinement for ill-conditioned A."""
    # TODO: Implement
    pass
```

---

### M4: Alias Method

**Objective**: Implement Walker's alias method for O(1) sampling from a discrete distribution.

```python
class AliasTable:
    """O(1) sampling from a discrete distribution using the alias method."""

    def __init__(self, probs: np.ndarray):
        """Build the alias table from probabilities."""
        # TODO: Implement
        pass

    def sample(self, rng: np.random.Generator) -> int:
        """Sample an index in O(1) time."""
        # TODO: Implement
        pass
```
