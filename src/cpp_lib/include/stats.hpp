#pragma once

#include <cmath>
#include <stdexcept>

namespace stats {

/**
 * Online computation of mean and variance using Welford's algorithm.
 *
 * This algorithm is numerically stable and computes mean and variance
 * in a single pass through the data.
 */
class WelfordAccumulator {
public:
    WelfordAccumulator() : n_(0), mean_(0.0), m2_(0.0) {}

    /**
     * Add a new observation.
     */
    void update(double x) {
        n_ += 1;
        double delta = x - mean_;
        mean_ += delta / n_;
        double delta2 = x - mean_;
        m2_ += delta * delta2;
    }

    /**
     * Return number of observations.
     */
    int count() const { return n_; }

    /**
     * Return current mean.
     */
    double mean() const { return mean_; }

    /**
     * Return current sample variance (n-1 denominator).
     *
     * @throws std::runtime_error if fewer than 2 observations.
     */
    double variance() const {
        if (n_ < 2) {
            throw std::runtime_error("Need at least 2 observations for variance");
        }
        return m2_ / (n_ - 1);
    }

    /**
     * Return current sample standard deviation.
     */
    double std() const {
        return std::sqrt(variance());
    }

    /**
     * Reset accumulator to initial state.
     */
    void reset() {
        n_ = 0;
        mean_ = 0.0;
        m2_ = 0.0;
    }

private:
    int n_;
    double mean_;
    double m2_;
};

}  // namespace stats
