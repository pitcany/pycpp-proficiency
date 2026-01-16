# Day 6: Reproducibility, Randomness, and State

**Language**: Python
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/d1ed8d3d176e4e95a2d8f8b2bdff069f)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Set random seeds for NumPy and Python's random module
- [ ] Use `np.random.Generator` for modern random number generation
- [ ] Understand when state persists across function calls
- [ ] Write reproducible simulation code
- [ ] Manage randomness in parallel computations

## Sections

### Random Seed Basics

Legacy seeding (avoid in new code):
```python
np.random.seed(42)  # Global state - avoid!
```

### Modern Random Number Generation

Using `np.random.Generator`:
```python
rng = np.random.default_rng(42)
samples = rng.standard_normal(100)

# Pass rng to functions for reproducibility
def my_simulation(rng: np.random.Generator):
    return rng.random(10)
```

### Python's random Module

For non-numerical randomness:
```python
import random
random.seed(42)
random.shuffle(my_list)

# Or create isolated state
my_rng = random.Random(42)
my_rng.choice(options)
```

### Stateful Functions

Understanding when state persists:
- Global variables
- Mutable default arguments
- Class instance variables
- Module-level caches

### Reproducible Simulations

Design patterns for reproducibility:
```python
def run_simulation(
    n_samples: int,
    n_iterations: int,
    seed: int = 42
) -> dict:
    rng = np.random.default_rng(seed)
    # All randomness flows from rng
    ...
```

### Parallel Randomness

Managing RNG in parallel code:
```python
from numpy.random import SeedSequence, default_rng

# Create independent streams for parallel workers
ss = SeedSequence(42)
child_seeds = ss.spawn(n_workers)
rngs = [default_rng(s) for s in child_seeds]
```

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Never use `np.random.seed()` - use `Generator`
2. Pass `rng` as a function parameter
3. Use `SeedSequence` for parallel reproducibility
4. Document seed requirements in function signatures

## Next Steps

Proceed to [Day 7: Debugging, Profiling, and Python Capstone](../day-07/README.md).
