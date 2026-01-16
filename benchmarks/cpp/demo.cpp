/**
 * Demo program for C++ course utilities.
 */

#include <iostream>
#include <vector>
#include <random>
#include <chrono>

#include "numerical.hpp"
#include "stats.hpp"

int main() {
    std::cout << "=== pycpp-proficiency C++ Demo ===\n\n";

    // Test Welford's algorithm
    std::cout << "1. Welford's Algorithm\n";
    stats::WelfordAccumulator acc;
    std::vector<double> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    for (double x : data) {
        acc.update(x);
    }
    std::cout << "   Data: 1, 2, ..., 10\n";
    std::cout << "   Mean: " << acc.mean() << " (expected: 5.5)\n";
    std::cout << "   Variance: " << acc.variance() << " (expected: 9.166...)\n";
    std::cout << "   Std: " << acc.std() << "\n\n";

    // Test log-sum-exp
    std::cout << "2. Log-Sum-Exp (Numerical Stability)\n";
    std::vector<double> large_values = {1000, 1000, 1000};
    double lse = numerical::log_sum_exp(large_values);
    std::cout << "   Input: [1000, 1000, 1000]\n";
    std::cout << "   log_sum_exp: " << lse << " (expected: ~1001.1)\n\n";

    std::vector<double> small_values = {-1000, -1000, -1000};
    lse = numerical::log_sum_exp(small_values);
    std::cout << "   Input: [-1000, -1000, -1000]\n";
    std::cout << "   log_sum_exp: " << lse << " (expected: ~-998.9)\n\n";

    // Test Kahan summation
    std::cout << "3. Kahan Summation\n";
    std::vector<double> kahan_test;
    kahan_test.push_back(1e16);
    for (int i = 0; i < 10000; ++i) {
        kahan_test.push_back(1.0);
    }
    double naive_sum = 0;
    for (double x : kahan_test) naive_sum += x;
    double kahan = numerical::kahan_sum(kahan_test);
    std::cout << "   Input: 1e16 + 10000 ones\n";
    std::cout << "   Naive sum: " << naive_sum << "\n";
    std::cout << "   Kahan sum: " << kahan << "\n";
    std::cout << "   Expected:  " << (1e16 + 10000) << "\n\n";

    // Performance test
    std::cout << "4. Performance (1M random numbers)\n";
    std::mt19937 rng(42);
    std::normal_distribution<double> dist(0.0, 1.0);
    std::vector<double> large_data(1000000);
    for (auto& x : large_data) x = dist(rng);

    auto start = std::chrono::high_resolution_clock::now();
    stats::WelfordAccumulator perf_acc;
    for (double x : large_data) perf_acc.update(x);
    auto end = std::chrono::high_resolution_clock::now();
    auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    std::cout << "   Welford mean: " << perf_acc.mean() << "\n";
    std::cout << "   Welford variance: " << perf_acc.variance() << "\n";
    std::cout << "   Time: " << ms.count() << " ms\n\n";

    std::cout << "=== Demo Complete ===\n";
    return 0;
}
