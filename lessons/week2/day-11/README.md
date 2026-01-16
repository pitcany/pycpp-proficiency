# Day 11: STL Containers, Algorithms, and Iterators

**Language**: C++
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/0626a6141dcb4595a24d95c25a2580e5)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Choose appropriate containers for different use cases
- [ ] Use STL algorithms to replace raw loops
- [ ] Understand iterator categories and invalidation
- [ ] Write lambdas for use with algorithms
- [ ] Compose operations using algorithm chaining

## Sections

### Containers: Choosing the Right Data Structure

| Container | Access | Insert | Erase | Use Case |
|-----------|--------|--------|-------|----------|
| `vector` | O(1) | O(n) | O(n) | Default choice |
| `deque` | O(1) | O(1)* | O(1)* | Double-ended |
| `list` | O(n) | O(1) | O(1) | Frequent insert/erase |
| `set/map` | O(log n) | O(log n) | O(log n) | Ordered, unique |
| `unordered_set/map` | O(1)* | O(1)* | O(1)* | Fast lookup |

### Iterators: The Universal Pointer Abstraction

Categories (weakest to strongest):
1. Input/Output - single pass
2. Forward - multiple passes forward
3. Bidirectional - can go backward
4. Random Access - jump anywhere

### Algorithms: Generic, Composable, Efficient

Common algorithms:
```cpp
#include <algorithm>
#include <numeric>

std::sort(v.begin(), v.end());
auto it = std::find(v.begin(), v.end(), target);
int sum = std::accumulate(v.begin(), v.end(), 0);
std::transform(v.begin(), v.end(), v.begin(), [](int x) { return x * 2; });
```

### Lambdas: Inline Anonymous Functions

```cpp
auto add = [](int a, int b) { return a + b; };

// Capture by value
int multiplier = 2;
auto times = [multiplier](int x) { return x * multiplier; };

// Capture by reference
auto increment = [&counter]() { ++counter; };
```

### Algorithm Composition

Chaining algorithms for complex operations:
```cpp
// Find first even number > 10
auto it = std::find_if(v.begin(), v.end(),
    [](int x) { return x > 10 && x % 2 == 0; });
```

### Performance Considerations

- `vector` usually wins due to cache locality
- Reserve capacity to avoid reallocations
- Use `emplace` to construct in place

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Default to `vector`
2. Prefer algorithms over raw loops
3. Use lambdas for custom predicates
4. Know iterator invalidation rules

## Next Steps

Proceed to [Day 12: Numerical Stability and Floating-Point](../day-12/README.md).
