# Day 3: Broadcasting and Vectorization

**Language**: Python
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/4e025218f330406da7cf4dc073a75426)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Apply broadcasting rules to combine arrays of different shapes
- [ ] Vectorize computations to replace Python loops
- [ ] Use `np.newaxis` and reshape to control broadcasting
- [ ] Avoid common broadcasting pitfalls
- [ ] Benchmark vectorized vs loop-based code

## Sections

### Broadcasting Rules

NumPy's broadcasting semantics:
1. Arrays are compared shape from right to left
2. Dimensions are compatible if equal or one is 1
3. Missing dimensions are treated as 1
4. The output shape is the maximum along each dimension

Examples:
```python
(3, 4) + (4,)     -> (3, 4)  # OK
(3, 4) + (3, 1)   -> (3, 4)  # OK
(3, 4) + (3,)     -> Error   # Incompatible
```

### Controlling Broadcasting with newaxis

Adding dimensions for broadcasting:
```python
# Outer product via broadcasting
a = np.array([1, 2, 3])
b = np.array([10, 20])
outer = a[:, np.newaxis] * b  # Shape (3, 1) * (2,) = (3, 2)
```

### Vectorization

Replacing loops with array operations:
- Element-wise operations
- Reduction operations (sum, mean, max along axes)
- Outer operations using broadcasting
- Boolean indexing

### Common Pitfalls

Bugs and performance issues:
- Shape mismatch errors
- Unexpected broadcasting (silent bugs)
- Memory explosion from broadcasting large arrays
- When vectorization isn't worth it

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Broadcasting rules: compare shapes right-to-left
2. Use `np.newaxis` to add dimensions
3. Vectorized code can be 100x faster than loops
4. Check shapes to avoid silent broadcasting bugs

## Next Steps

Proceed to [Day 4: Pandas Pitfalls and Alternatives](../day-04/README.md).
