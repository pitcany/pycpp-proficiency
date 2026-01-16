# Day 2: Memory Model, Views, and Copies

**Language**: Python
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/414f937f149246e899a2fb2b2b482f4e)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Distinguish between shallow copies, deep copies, and references
- [ ] Predict when NumPy operations return views vs copies
- [ ] Debug unintended mutations in nested data structures
- [ ] Use `is` vs `==` correctly
- [ ] Understand object mutability and its implications

## Sections

### References vs Copies

Understanding Python's object model:
- Everything is an object
- Variables are references to objects
- Assignment creates references, not copies
- `id()` and identity vs equality

### Shallow vs Deep Copy

When you need actual copies:
- `copy.copy()` for shallow copies
- `copy.deepcopy()` for deep copies
- When each is appropriate
- Performance implications

### NumPy Views vs Copies

Critical for efficient numerical computing:
- Slicing creates views
- Advanced indexing creates copies
- `.copy()` to force a copy
- Checking with `.flags['OWNDATA']` and `np.shares_memory()`

### Common Pitfalls

Bugs you'll encounter:
- Mutable default arguments
- Modifying lists while iterating
- Unintended aliasing in function arguments
- Nested list mutations

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Assignment creates references, not copies
2. NumPy slices are views (fast but dangerous)
3. Use `np.shares_memory()` to check for aliasing
4. When in doubt, make an explicit copy

## Next Steps

Proceed to [Day 3: Broadcasting and Vectorization](../day-03/README.md).
