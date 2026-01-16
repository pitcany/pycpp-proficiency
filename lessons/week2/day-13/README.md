# Day 13: Performance Reasoning and Optimization

**Language**: C++
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/fc944ca11d284611ae4a853c384dd7e2)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Understand the memory hierarchy (cache, RAM, disk)
- [ ] Reason about cache-friendly vs cache-hostile code
- [ ] Use profiling tools to identify bottlenecks
- [ ] Apply Amdahl's law to predict speedups
- [ ] Benchmark code correctly

## Sections

### Memory Hierarchy

Latency (approximate):
- L1 cache: ~1 ns
- L2 cache: ~4 ns
- L3 cache: ~10 ns
- RAM: ~100 ns
- SSD: ~100,000 ns
- HDD: ~10,000,000 ns

Key insight: Memory access patterns dominate performance.

### Data Layout Matters

Row-major vs column-major:
```cpp
// Cache-friendly: access consecutive memory
for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
        A[i][j] = 0;  // Row-major: good

// Cache-hostile: strided access
for (int j = 0; j < M; ++j)
    for (int i = 0; i < N; ++i)
        A[i][j] = 0;  // Column access in row-major: bad
```

### Compiler Optimizations

Common optimizations:
- Inlining
- Loop unrolling
- Vectorization (SIMD)
- Dead code elimination
- Constant propagation

Flags: `-O0`, `-O1`, `-O2`, `-O3`, `-Ofast`

### Profiling

Tools:
- `perf` (Linux)
- `Instruments` (macOS)
- `gprof`
- `valgrind --tool=callgrind`

```bash
# Basic profiling
perf record ./myprogram
perf report
```

### Benchmarking

Rules for valid benchmarks:
1. Warm up caches
2. Multiple iterations
3. Prevent dead code elimination
4. Statistical analysis

```cpp
// Prevent optimization away
volatile auto result = compute();
```

### Amdahl's Law

Speedup limited by sequential portion:
```
Speedup = 1 / ((1-P) + P/S)
```
Where P = parallelizable fraction, S = speedup of parallel part.

### Optimization Strategies

1. Measure first (profile)
2. Optimize hot paths only
3. Improve data locality
4. Reduce allocations
5. Use SIMD when applicable

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Memory access patterns dominate performance
2. Always profile before optimizing
3. Amdahl's law limits parallel speedup
4. Most code doesn't need optimization

## Next Steps

Proceed to [Day 14: C++ Capstone and Cross-Language Integration](../day-14/README.md).
