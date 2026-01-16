# Day 14: C++ Capstone and Cross-Language Integration

**Language**: C++
**Time Estimate**: 6-8 hours (capstone: 4-6 hours)
**Notion Source**: [Link](https://www.notion.so/64ebf681f77a4ec5a6cd53d0d10c774a)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Complete a comprehensive C++ capstone project
- [ ] Use pybind11 to expose C++ functions to Python
- [ ] Pass NumPy arrays between Python and C++
- [ ] Understand when to use C++ vs Python
- [ ] Demonstrate proficiency in all Week 2 skills

## Sections

### Python vs C++: When to Use Each

Use Python for:
- Rapid prototyping
- Data exploration
- Orchestration
- I/O and glue code

Use C++ for:
- Inner loops
- Memory-constrained code
- Real-time requirements
- Existing C++ libraries

### Cross-Language Integration with pybind11

Basic binding:
```cpp
#include <pybind11/pybind11.h>

double add(double a, double b) {
    return a + b;
}

PYBIND11_MODULE(mymodule, m) {
    m.def("add", &add, "Add two numbers");
}
```

### Passing NumPy Arrays

```cpp
#include <pybind11/numpy.h>

namespace py = pybind11;

double sum_array(py::array_t<double> arr) {
    auto r = arr.unchecked<1>();  // 1D array
    double sum = 0;
    for (ssize_t i = 0; i < r.shape(0); ++i) {
        sum += r(i);
    }
    return sum;
}
```

### Performance Comparison

When C++ provides speedup:
- Loops that can't be vectorized
- Complex control flow
- Memory-intensive operations
- Recursive algorithms

When Python is fast enough:
- NumPy/Pandas operations
- I/O-bound code
- Simple transformations

### When C++ is Worth It

Consider C++ when:
- Profile shows Python is bottleneck
- Operation must run >1000x/second
- Need deterministic timing
- Memory usage is critical

## C++ Capstone: Gaussian Mixture Model Fitting

**Time**: 4-6 hours

Build a complete GMM implementation demonstrating all Week 2 skills.

### Requirements

1. **Data Structures**: Matrix and Vector classes with RAII
2. **EM Algorithm**: E-step and M-step with log-sum-exp stability
3. **STL Usage**: Containers and algorithms throughout
4. **Cache-Friendly**: Memory layout optimized for access patterns
5. **Profiling**: E-step and M-step profiled separately
6. **Python Binding**: Exposed via pybind11
7. **NumPy Integration**: Accept/return NumPy arrays
8. **Testing**: Unit tests for each component
9. **Validation**: Verify against sklearn
10. **Performance**: <1s for 10K points, 20 dimensions, 5 components

### Rubric Dimensions

- Data Structures
- EM Algorithm
- Testing
- Performance
- Python Binding
- sklearn Match
- Documentation

See [exercises.md](exercises.md) for full specification.

## Key Takeaways

1. C++ for performance-critical inner loops
2. pybind11 makes integration straightforward
3. Profile to identify where C++ helps
4. Both languages have their strengths

## Next Steps

Congratulations on completing Week 2! Optionally continue to [Week 3: Optional Extensions](../../week3/day-15/README.md).
