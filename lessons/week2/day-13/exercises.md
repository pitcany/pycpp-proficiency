# Day 13: Performance Reasoning and Optimization - Exercises

## Foundational Exercises

### Exercise 13.1: Cache-Friendly Matrix Multiplication

**Objective**: Implement matrix multiplication with good cache behavior.

```cpp
#include <vector>
#include <chrono>
#include <iostream>

using Matrix = std::vector<std::vector<double>>;

// Naive implementation (cache-hostile for B)
void matmul_naive(const Matrix& A, const Matrix& B, Matrix& C) {
    int N = A.size();
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            double sum = 0;
            for (int k = 0; k < N; ++k) {
                sum += A[i][k] * B[k][j];  // B access is strided!
            }
            C[i][j] = sum;
        }
    }
}

// TODO: Cache-friendly version (reorder loops)
void matmul_cache_friendly(const Matrix& A, const Matrix& B, Matrix& C) {
    // Hint: Change loop order to i, k, j
    // This makes B access sequential
}

// TODO: Blocked version for even better cache usage
void matmul_blocked(const Matrix& A, const Matrix& B, Matrix& C, int block_size = 32) {
    // Divide matrix into blocks that fit in cache
}

// Benchmark
int main() {
    int N = 512;
    Matrix A(N, std::vector<double>(N, 1.0));
    Matrix B(N, std::vector<double>(N, 1.0));
    Matrix C(N, std::vector<double>(N, 0.0));

    auto benchmark = [&](auto fn, const char* name) {
        auto start = std::chrono::high_resolution_clock::now();
        fn(A, B, C);
        auto end = std::chrono::high_resolution_clock::now();
        auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        std::cout << name << ": " << ms.count() << " ms\n";
    };

    benchmark(matmul_naive, "Naive");
    benchmark(matmul_cache_friendly, "Cache-friendly");
    benchmark([](auto& a, auto& b, auto& c) { matmul_blocked(a, b, c, 32); }, "Blocked");

    return 0;
}
```

---

### Exercise 13.2: Profile and Optimize

**Objective**: Use profiling to identify and fix bottlenecks.

```cpp
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_set>

// This program has performance issues. Profile and optimize.

std::vector<std::string> process_data(const std::vector<std::string>& input) {
    std::vector<std::string> result;

    for (const auto& s : input) {
        // Issue 1: Repeated linear search
        bool found = false;
        for (const auto& r : result) {
            if (r == s) {
                found = true;
                break;
            }
        }
        if (!found) {
            result.push_back(s);
        }
    }

    // Issue 2: Inefficient sort comparison
    std::sort(result.begin(), result.end(),
        [](const std::string& a, const std::string& b) {
            return a.size() < b.size() ||
                   (a.size() == b.size() && a < b);
        });

    // Issue 3: String concatenation in loop
    for (auto& s : result) {
        s = "[" + s + "]";
    }

    return result;
}

// TODO: Optimized version
std::vector<std::string> process_data_optimized(const std::vector<std::string>& input) {
    // Use unordered_set for deduplication
    // Use reserve() for vectors
    // Minimize string copies
}
```

---

### Exercise 13.3: Apply Amdahl's Law

**Objective**: Predict parallel speedup and validate.

```cpp
// Given:
// - Total execution time: 100 seconds
// - 80% of time spent in parallelizable section
// - You have 4 cores

// Q1: What is the maximum speedup with 4 cores?
// Speedup = 1 / ((1 - 0.8) + 0.8/4) = 1 / (0.2 + 0.2) = 2.5x

// Q2: What if you had infinite cores?
// Speedup = 1 / (1 - 0.8) = 5x (limited by sequential 20%)

// Q3: You optimize the sequential part to take half the time.
//     Now 10% is sequential, 90% parallelizable.
//     What's the new speedup with 4 cores?

// TODO: Implement and verify
#include <iostream>
#include <thread>
#include <chrono>
#include <vector>

void sequential_work(int ms) {
    std::this_thread::sleep_for(std::chrono::milliseconds(ms));
}

void parallel_work(int ms, int n_threads) {
    std::vector<std::thread> threads;
    int per_thread = ms / n_threads;

    for (int i = 0; i < n_threads; ++i) {
        threads.emplace_back([per_thread]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(per_thread));
        });
    }
    for (auto& t : threads) t.join();
}

int main() {
    int seq_time = 200;  // 20% of 1000ms
    int par_time = 800;  // 80% of 1000ms

    // Serial execution
    auto start = std::chrono::high_resolution_clock::now();
    sequential_work(seq_time);
    sequential_work(par_time);
    auto serial_time = std::chrono::high_resolution_clock::now() - start;

    // Parallel execution (4 threads)
    start = std::chrono::high_resolution_clock::now();
    sequential_work(seq_time);
    parallel_work(par_time, 4);
    auto parallel_time = std::chrono::high_resolution_clock::now() - start;

    // Calculate actual speedup
    double speedup = /* TODO */;
    std::cout << "Actual speedup: " << speedup << "x\n";
    std::cout << "Predicted (Amdahl): 2.5x\n";

    return 0;
}
```

---

## Proficiency Exercises

### Exercise 13.4: Memory Access Patterns

**Objective**: Analyze and optimize memory access patterns.

```cpp
#include <vector>
#include <chrono>
#include <iostream>
#include <random>

// Array of Structures (AoS)
struct ParticleAoS {
    double x, y, z;
    double vx, vy, vz;
    double mass;
    int id;
};

// Structure of Arrays (SoA)
struct ParticlesSoA {
    std::vector<double> x, y, z;
    std::vector<double> vx, vy, vz;
    std::vector<double> mass;
    std::vector<int> id;
};

// Task: Compute total kinetic energy = 0.5 * mass * v²

// AoS version
double kinetic_energy_aos(const std::vector<ParticleAoS>& particles) {
    double total = 0;
    for (const auto& p : particles) {
        double v2 = p.vx*p.vx + p.vy*p.vy + p.vz*p.vz;
        total += 0.5 * p.mass * v2;
    }
    return total;
}

// TODO: SoA version - should be faster due to better cache usage
double kinetic_energy_soa(const ParticlesSoA& particles) {
}

// Benchmark both and explain the difference
```

---

### Exercise 13.5: Benchmarking Best Practices

**Objective**: Write correct benchmarks.

```cpp
#include <chrono>
#include <vector>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <cmath>

template<typename Func>
auto benchmark(Func fn, int warmup = 3, int iterations = 10) {
    // TODO: Implement proper benchmarking
    // 1. Run warmup iterations (don't measure)
    // 2. Run measured iterations
    // 3. Return statistics (mean, stddev, min, max)

    struct Stats {
        double mean_ms;
        double stddev_ms;
        double min_ms;
        double max_ms;
    };

    // Warmup
    for (int i = 0; i < warmup; ++i) {
        fn();
    }

    // Measure
    std::vector<double> times;
    for (int i = 0; i < iterations; ++i) {
        auto start = std::chrono::high_resolution_clock::now();
        fn();
        auto end = std::chrono::high_resolution_clock::now();
        auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
        times.push_back(ns.count() / 1e6);  // Convert to ms
    }

    // TODO: Compute stats
    Stats stats;
    return stats;
}

// Prevent dead code elimination
template<typename T>
void do_not_optimize(T& value) {
    asm volatile("" : : "r,m"(value) : "memory");
}
```

---

## Mastery Exercises

### Exercise 13.6: SIMD Optimization

**Objective**: Manually vectorize a computation.

```cpp
#include <vector>
#include <chrono>
#include <iostream>

// Scalar version
void add_vectors_scalar(const float* a, const float* b, float* c, size_t n) {
    for (size_t i = 0; i < n; ++i) {
        c[i] = a[i] + b[i];
    }
}

// TODO: SIMD version using intrinsics (x86)
// #include <immintrin.h>
void add_vectors_simd(const float* a, const float* b, float* c, size_t n) {
    // Use _mm256_load_ps, _mm256_add_ps, _mm256_store_ps
    // Process 8 floats at a time with AVX
}

// Alternative: Let compiler vectorize
void add_vectors_auto(const float* __restrict a,
                      const float* __restrict b,
                      float* __restrict c, size_t n) {
    // __restrict helps compiler prove no aliasing
    #pragma omp simd
    for (size_t i = 0; i < n; ++i) {
        c[i] = a[i] + b[i];
    }
}
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Cache optimization | No improvement | Some improvement | Significant speedup |
| Profiling | Cannot profile | Basic usage | Identifies real bottlenecks |
| Amdahl's law | Cannot apply | Basic application | Accurate predictions |
| Benchmarking | Invalid benchmark | Correct but basic | Professional quality |
