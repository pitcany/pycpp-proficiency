# Day 7: Debugging, Profiling, and Python Capstone

**Language**: Python
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/7a503edf4cb340788f748748b3d6d2f6)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Use pdb and IDE debuggers effectively
- [ ] Instrument code with logging instead of print statements
- [ ] Profile code to identify bottlenecks
- [ ] Optimize slow code using profiling insights
- [ ] Complete the Week 1 Python capstone project

## Sections

### Debugging with pdb

Python's built-in debugger:
```python
import pdb; pdb.set_trace()  # Breakpoint

# Or use breakpoint() in Python 3.7+
breakpoint()

# Common commands:
# n - next line
# s - step into
# c - continue
# p expr - print expression
# l - list source
# q - quit
```

### Logging

Production-ready output:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

logger.info("Starting computation")
logger.debug("x = %s", x)  # Lazy formatting
logger.warning("Unusual value detected")
logger.error("Computation failed", exc_info=True)
```

### Profiling

Finding bottlenecks:
```python
# cProfile for function-level profiling
import cProfile
cProfile.run('my_function()')

# line_profiler for line-by-line
# @profile decorator, run with kernprof

# memory_profiler for memory usage
# @profile decorator, run with python -m memory_profiler
```

### Optimization Strategies

After profiling:
1. Vectorize loops
2. Use appropriate data structures
3. Reduce memory allocation
4. Consider Numba/Cython for hot loops

## Week 1 Python Capstone

**Title**: Statistical Analysis Pipeline

**Time**: 90-120 minutes

### Requirements

Build a complete statistical analysis pipeline that demonstrates all Week 1 skills:

1. **Code Quality**: Create reusable module with type-hinted functions
2. **Resource Management**: Use context managers for file I/O
3. **Memory Safety**: Correctly handle NumPy views and copies
4. **Vectorization**: No Python loops over data
5. **Pandas Best Practices**: Use .loc (no chained indexing)
6. **Testing**: Unit tests with pytest (>80% coverage)
7. **Reproducibility**: Accept rng parameter for all random operations
8. **Logging**: Use logging instead of print statements
9. **Performance**: Profile code and optimize bottlenecks

### Rubric Dimensions

- Code Quality
- Functionality
- Best Practices
- Testing

See [exercises.md](exercises.md) for the full capstone specification.

## Next Steps

Congratulations on completing Week 1!

**If you have never written C++ before**, complete [Day 7.5: C++ Primer](../../week2/cpp-primer/README.md) before starting Week 2.

**If you're comfortable with basic C++ syntax**, proceed directly to [Day 8: References, Pointers, and Ownership](../../week2/day-08/README.md).
