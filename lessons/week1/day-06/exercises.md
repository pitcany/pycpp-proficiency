# Day 6: Reproducibility, Randomness, and State - Exercises

## Foundational Exercises

### Exercise 6.1: Debug Reproducibility

**Objective**: Fix reproducibility bugs in simulation code.

```python
import numpy as np

# Bug 1: Uses global state
def simulate_walk():
    np.random.seed(42)  # Wrong place!
    steps = np.random.choice([-1, 1], size=100)
    return np.cumsum(steps)

# Problem: Running twice gives same results
# But calling another random function between calls breaks it

# Bug 2: Mutable default creates shared state
def accumulate_samples(n: int, samples: list = []):
    samples.extend(np.random.randn(n).tolist())
    return samples

# Problem: samples persists between calls

# Bug 3: Random state not passed through
def monte_carlo_pi(n_samples: int) -> float:
    x = np.random.random(n_samples)
    y = np.random.random(n_samples)
    inside = (x**2 + y**2) <= 1
    return 4 * inside.mean()

# Problem: Results not reproducible

# TODO: Fix all three functions
```

---

### Exercise 6.2: Implement Reproducible Bootstrap

**Objective**: Write a reproducible bootstrap function.

```python
import numpy as np
from typing import Callable

def bootstrap_statistic(
    data: np.ndarray,
    statistic: Callable[[np.ndarray], float],
    n_bootstrap: int = 1000,
    rng: np.random.Generator | None = None
) -> np.ndarray:
    """
    Compute bootstrap distribution of a statistic.

    Args:
        data: Original sample
        statistic: Function that computes statistic from sample
        n_bootstrap: Number of bootstrap samples
        rng: Random generator for reproducibility

    Returns:
        Array of bootstrap statistics
    """
    # TODO: Implement
    # 1. Handle rng being None (create default)
    # 2. Generate bootstrap samples
    # 3. Compute statistic for each
    pass

# Test reproducibility
rng1 = np.random.default_rng(42)
rng2 = np.random.default_rng(42)

data = np.array([1, 2, 3, 4, 5])
result1 = bootstrap_statistic(data, np.mean, rng=rng1)
result2 = bootstrap_statistic(data, np.mean, rng=rng2)

assert np.allclose(result1, result2)  # Must be identical
```

---

## Proficiency Exercises

### Exercise 6.3: Parallel Reproducibility

**Objective**: Implement reproducible parallel simulation.

```python
import numpy as np
from numpy.random import SeedSequence, default_rng
from concurrent.futures import ProcessPoolExecutor
from typing import Callable

def worker_simulation(
    worker_id: int,
    seed: SeedSequence,
    n_samples: int
) -> float:
    """Run one worker's simulation."""
    rng = default_rng(seed)
    # Simulate random walk
    steps = rng.choice([-1, 1], size=n_samples)
    return np.cumsum(steps)[-1]

def parallel_simulation(
    n_workers: int,
    n_samples_per_worker: int,
    base_seed: int = 42
) -> list[float]:
    """
    Run simulation across multiple workers reproducibly.

    Each worker should get an independent, reproducible RNG.
    """
    # TODO: Implement
    # 1. Create SeedSequence from base_seed
    # 2. Spawn child seeds for each worker
    # 3. Run workers in parallel
    # 4. Collect and return results
    pass

# Test: Same base_seed should give same results
result1 = parallel_simulation(4, 1000, base_seed=42)
result2 = parallel_simulation(4, 1000, base_seed=42)
assert result1 == result2
```

---

### Exercise 6.4: Simulation Framework

**Objective**: Build a reproducible simulation framework.

```python
import numpy as np
from dataclasses import dataclass
from typing import Any

@dataclass
class SimulationConfig:
    """Configuration for a simulation run."""
    n_samples: int
    n_iterations: int
    seed: int
    # Add more parameters as needed

@dataclass
class SimulationResult:
    """Results from a simulation run."""
    config: SimulationConfig
    estimates: np.ndarray
    # Add more result fields as needed

class Simulation:
    """Base class for reproducible simulations."""

    def __init__(self, config: SimulationConfig):
        self.config = config
        self.rng = np.random.default_rng(config.seed)

    def run(self) -> SimulationResult:
        """Run the simulation and return results."""
        raise NotImplementedError

# TODO: Implement a concrete simulation
class MonteCarloIntegration(Simulation):
    """Monte Carlo integration of a function."""

    def __init__(self, config: SimulationConfig, func: callable, bounds: tuple):
        super().__init__(config)
        self.func = func
        self.bounds = bounds

    def run(self) -> SimulationResult:
        # TODO: Implement
        pass
```

---

## Mastery Exercises

### Exercise 6.5: Checkpointing and Resume

**Objective**: Implement simulation with checkpoint/resume capability.

```python
import numpy as np
import json
from pathlib import Path

class CheckpointedSimulation:
    """
    Simulation that can be stopped and resumed.

    Saves RNG state and partial results to disk.
    """

    def __init__(self, seed: int, checkpoint_dir: Path):
        self.seed = seed
        self.checkpoint_dir = checkpoint_dir
        self.rng = np.random.default_rng(seed)
        self.iteration = 0
        self.results = []

    def save_checkpoint(self):
        """Save current state to disk."""
        # TODO: Save rng state, iteration, results
        pass

    def load_checkpoint(self) -> bool:
        """Load state from disk. Returns True if checkpoint exists."""
        # TODO: Restore rng state, iteration, results
        pass

    def run(self, n_iterations: int, checkpoint_every: int = 100):
        """Run simulation with periodic checkpointing."""
        # TODO: Implement with checkpointing
        pass
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Global state | Uses np.random.seed | Partial fix | All Generator-based |
| Reproducibility | Not reproducible | Partially reproducible | Fully reproducible |
| Parallel safety | Not safe | Basic safety | SeedSequence used |
| API design | Poor | Acceptable | Clean, documented |
