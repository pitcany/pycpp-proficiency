# Day 12: Numerical Stability and Floating-Point

**Language**: C++
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/47266ef05f25405a9676dcd3392dc0b8)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Understand IEEE 754 floating-point representation
- [ ] Avoid catastrophic cancellation in computations
- [ ] Implement stable variance and summation algorithms
- [ ] Use log-space computation to avoid overflow
- [ ] Compare floating-point numbers correctly

## Sections

### Floating-Point Representation

IEEE 754 double precision:
- 1 sign bit
- 11 exponent bits
- 52 mantissa bits
- Range: ±2.2e-308 to ±1.8e308
- Precision: ~15-17 significant digits

Special values: `+inf`, `-inf`, `NaN`, `-0`

### Catastrophic Cancellation

When subtracting nearly equal numbers:
```cpp
double bad = (1e16 + 1) - 1e16;  // Expected: 1, Actual: 0

// Example: Computing variance
// Bad: Var = E[X²] - E[X]² (catastrophic cancellation)
// Good: Welford's algorithm
```

### Summation Stability

Naive summation accumulates error:
```cpp
// Bad: Many small numbers added to large accumulator
double sum = 0;
for (double x : values) sum += x;  // Error grows

// Good: Kahan summation
double sum = 0, c = 0;
for (double x : values) {
    double y = x - c;
    double t = sum + y;
    c = (t - sum) - y;
    sum = t;
}
```

### Log-Space Computation

Avoid overflow/underflow with log-space:
```cpp
// Bad: p1 * p2 * p3 (underflows quickly)
// Good: log(p1) + log(p2) + log(p3)

// Log-sum-exp trick:
// log(sum(exp(x_i))) = max(x) + log(sum(exp(x_i - max(x))))
```

### Comparing Floating-Point Numbers

Never use `==` for floats:
```cpp
// Bad
if (a == b) { ... }

// Good: Absolute tolerance
if (std::abs(a - b) < epsilon) { ... }

// Better: Relative tolerance
if (std::abs(a - b) < epsilon * std::max(std::abs(a), std::abs(b))) { ... }
```

### Overflow and Underflow

Avoiding numerical extremes:
- Work in log-space
- Normalize intermediate values
- Use stable algorithms

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Floating-point has finite precision
2. Avoid subtracting nearly equal numbers
3. Use stable algorithms (Welford, Kahan)
4. Work in log-space for products of probabilities

## Next Steps

Proceed to [Day 13: Performance Reasoning and Optimization](../day-13/README.md).
