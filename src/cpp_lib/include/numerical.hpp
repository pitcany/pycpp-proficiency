#pragma once

#include <algorithm>
#include <cmath>
#include <limits>
#include <vector>

namespace numerical {

/**
 * Compute log(sum(exp(x))) in a numerically stable way.
 *
 * Uses the log-sum-exp trick to avoid overflow/underflow.
 */
inline double log_sum_exp(const std::vector<double>& x) {
    if (x.empty()) {
        return -std::numeric_limits<double>::infinity();
    }

    double max_val = *std::max_element(x.begin(), x.end());

    if (!std::isfinite(max_val)) {
        return max_val;
    }

    double sum = 0.0;
    for (double xi : x) {
        sum += std::exp(xi - max_val);
    }

    return max_val + std::log(sum);
}

/**
 * Compute log(sum(exp(x))) for a raw array.
 */
inline double log_sum_exp(const double* x, size_t n) {
    if (n == 0) {
        return -std::numeric_limits<double>::infinity();
    }

    double max_val = x[0];
    for (size_t i = 1; i < n; ++i) {
        if (x[i] > max_val) max_val = x[i];
    }

    if (!std::isfinite(max_val)) {
        return max_val;
    }

    double sum = 0.0;
    for (size_t i = 0; i < n; ++i) {
        sum += std::exp(x[i] - max_val);
    }

    return max_val + std::log(sum);
}

/**
 * Compute stable softmax in-place.
 */
inline void softmax_inplace(std::vector<double>& x) {
    if (x.empty()) return;

    double max_val = *std::max_element(x.begin(), x.end());
    double sum = 0.0;

    for (double& xi : x) {
        xi = std::exp(xi - max_val);
        sum += xi;
    }

    for (double& xi : x) {
        xi /= sum;
    }
}

/**
 * Kahan compensated summation for reduced floating-point error.
 */
inline double kahan_sum(const std::vector<double>& x) {
    double sum = 0.0;
    double c = 0.0;  // Compensation for lost low-order bits

    for (double xi : x) {
        double y = xi - c;
        double t = sum + y;
        c = (t - sum) - y;
        sum = t;
    }

    return sum;
}

/**
 * Compare floating-point numbers with relative and absolute tolerance.
 */
inline bool approx_equal(double a, double b,
                         double rel_tol = 1e-9,
                         double abs_tol = 0.0) {
    if (std::isnan(a) || std::isnan(b)) {
        return false;
    }
    if (std::isinf(a) && std::isinf(b)) {
        return (a > 0) == (b > 0);  // Same sign infinity
    }

    double diff = std::abs(a - b);
    return diff <= std::max(rel_tol * std::max(std::abs(a), std::abs(b)), abs_tol);
}

}  // namespace numerical
