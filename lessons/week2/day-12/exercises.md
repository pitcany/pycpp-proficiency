# Day 12: Numerical Stability and Floating-Point - Exercises

## Foundational Exercises

### Exercise 12.1: Implement Welford's Algorithm

**Objective**: Implement numerically stable online mean and variance.

```cpp
#include <cmath>
#include <iostream>
#include <vector>

class OnlineStats {
private:
    int n_;
    double mean_;
    double M2_;  // Sum of squared differences from mean

public:
    OnlineStats() : n_(0), mean_(0.0), M2_(0.0) {}

    void update(double x) {
        // TODO: Implement Welford's algorithm
        // n_ += 1
        // delta = x - mean_
        // mean_ += delta / n_
        // delta2 = x - mean_
        // M2_ += delta * delta2
    }

    int count() const { return n_; }
    double mean() const { return mean_; }

    double variance() const {
        // TODO: Return sample variance (n-1 denominator)
        // Handle n < 2 case
    }

    double std_dev() const {
        return std::sqrt(variance());
    }
};

// Compare with naive implementation
class NaiveStats {
    std::vector<double> values_;
public:
    void update(double x) { values_.push_back(x); }

    double variance() const {
        // Naive: compute mean, then sum of squared differences
        // This has numerical issues with large values
        double mean = 0;
        for (double x : values_) mean += x;
        mean /= values_.size();

        double var = 0;
        for (double x : values_) var += (x - mean) * (x - mean);
        return var / (values_.size() - 1);
    }
};

int main() {
    // Test with values that expose numerical issues
    OnlineStats online;
    NaiveStats naive;

    // Large baseline with small variations
    double baseline = 1e9;
    for (int i = 0; i < 1000; ++i) {
        double x = baseline + (i % 10);
        online.update(x);
        naive.update(x);
    }

    std::cout << "Online variance: " << online.variance() << std::endl;
    std::cout << "Naive variance: " << naive.variance() << std::endl;
    // The naive version will show numerical errors

    return 0;
}
```

---

### Exercise 12.2: Implement Log-Sum-Exp

**Objective**: Implement stable log-sum-exp.

```cpp
#include <algorithm>
#include <cmath>
#include <limits>
#include <vector>

// Naive (unstable)
double log_sum_exp_naive(const std::vector<double>& x) {
    double sum = 0;
    for (double xi : x) {
        sum += std::exp(xi);  // Overflow if xi large!
    }
    return std::log(sum);  // Underflow if sum tiny!
}

// TODO: Stable implementation
double log_sum_exp(const std::vector<double>& x) {
    // 1. Find max
    // 2. Compute log(sum(exp(x_i - max)))
    // 3. Add max back
}

// Test
int main() {
    // Should work without overflow
    std::vector<double> large = {1000, 1000, 1000};
    std::cout << "Log-sum-exp (large): " << log_sum_exp(large) << std::endl;
    // Expected: ~1000 + log(3) ≈ 1001.1

    // Should work without underflow
    std::vector<double> small = {-1000, -1000, -1000};
    std::cout << "Log-sum-exp (small): " << log_sum_exp(small) << std::endl;
    // Expected: ~-1000 + log(3) ≈ -998.9

    return 0;
}
```

---

### Exercise 12.3: Kahan Summation

**Objective**: Implement compensated summation.

```cpp
#include <iostream>
#include <vector>
#include <cmath>

// Naive summation
double naive_sum(const std::vector<double>& x) {
    double sum = 0;
    for (double xi : x) sum += xi;
    return sum;
}

// TODO: Kahan summation
double kahan_sum(const std::vector<double>& x) {
    double sum = 0;
    double c = 0;  // Compensation for lost low-order bits

    for (double xi : x) {
        // TODO: Implement Kahan's algorithm
        // y = xi - c
        // t = sum + y
        // c = (t - sum) - y
        // sum = t
    }

    return sum;
}

int main() {
    // Create a case where naive summation loses precision
    std::vector<double> values;
    values.push_back(1e16);
    for (int i = 0; i < 10000; ++i) {
        values.push_back(1.0);
    }

    double naive = naive_sum(values);
    double kahan = kahan_sum(values);

    std::cout << "Expected: " << (1e16 + 10000) << std::endl;
    std::cout << "Naive:    " << naive << std::endl;
    std::cout << "Kahan:    " << kahan << std::endl;

    return 0;
}
```

---

## Proficiency Exercises

### Exercise 12.4: Stable Softmax

**Objective**: Implement numerically stable softmax.

```cpp
#include <vector>
#include <cmath>
#include <algorithm>

// Naive (unstable)
std::vector<double> softmax_naive(const std::vector<double>& x) {
    std::vector<double> result(x.size());
    double sum = 0;
    for (double xi : x) sum += std::exp(xi);  // Overflow!
    for (size_t i = 0; i < x.size(); ++i) {
        result[i] = std::exp(x[i]) / sum;
    }
    return result;
}

// TODO: Stable implementation
std::vector<double> softmax(const std::vector<double>& x) {
    // Hint: Subtract max before exponentiating
}

// TODO: Implement log-softmax (even more stable)
std::vector<double> log_softmax(const std::vector<double>& x) {
    // Returns log of softmax values
    // log(softmax(x_i)) = x_i - log_sum_exp(x)
}
```

---

### Exercise 12.5: Floating-Point Comparison

**Objective**: Implement robust floating-point comparison.

```cpp
#include <cmath>
#include <limits>

// TODO: Implement comparison functions

bool approx_equal_abs(double a, double b, double epsilon) {
    // Absolute tolerance
}

bool approx_equal_rel(double a, double b, double epsilon) {
    // Relative tolerance
}

bool approx_equal(double a, double b,
                  double rel_tol = 1e-9,
                  double abs_tol = 0.0) {
    // Combined: like Python's math.isclose
    // |a - b| <= max(rel_tol * max(|a|, |b|), abs_tol)
}

// Test edge cases
int main() {
    // Near zero
    assert(approx_equal(0.0, 1e-15, 1e-9, 1e-12));

    // Large numbers
    assert(approx_equal(1e10, 1e10 + 1, 1e-9));

    // Opposite signs
    assert(!approx_equal(1e-10, -1e-10, 1e-9, 0));

    // NaN handling
    assert(!approx_equal(NAN, NAN, 1e-9));

    // Infinity
    assert(approx_equal(INFINITY, INFINITY, 1e-9));

    return 0;
}
```

---

## Mastery Exercises

### Exercise 12.6: Stable Matrix Operations

**Objective**: Implement numerically stable matrix operations.

```cpp
#include <vector>
#include <cmath>

using Matrix = std::vector<std::vector<double>>;

// Stable log-determinant using LU decomposition
// (Avoid computing determinant directly - can overflow)
double log_det(const Matrix& A) {
    // TODO: Compute log|det(A)| stably
    // Use LU decomposition, sum log of diagonal elements
}

// Stable computation of log of multivariate normal density
double log_mvn_density(
    const std::vector<double>& x,
    const std::vector<double>& mean,
    const Matrix& cov
) {
    // TODO: Compute log N(x | mean, cov) without overflow/underflow
    // log N = -0.5 * (d * log(2π) + log|Σ| + (x-μ)ᵀ Σ⁻¹ (x-μ))
}
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Welford's algorithm | Wrong | Works but incomplete | Correct with edge cases |
| Log-sum-exp | Overflow/underflow | Stable | Handles all edge cases |
| Kahan summation | Wrong | Correct | Optimal |
| Understanding | Cannot explain issues | Basic understanding | Deep understanding |
