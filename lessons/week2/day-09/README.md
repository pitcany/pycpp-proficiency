# Day 9: Smart Pointers and Ownership Semantics

**Language**: C++
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/dc952dcf593f4220a6ac047fc16133e7)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Use `std::unique_ptr` for exclusive ownership
- [ ] Use `std::shared_ptr` for shared ownership
- [ ] Use `std::weak_ptr` to break reference cycles
- [ ] Understand when each smart pointer is appropriate
- [ ] Implement the Rule of Three (or Rule of Zero)
- [ ] Avoid memory leaks through RAII

## Sections

### Why Smart Pointers?

Raw pointers are error-prone:
```cpp
void dangerous() {
    int* p = new int(42);
    if (some_condition) return;  // Memory leak!
    delete p;
}
```

Smart pointers automate cleanup.

### std::unique_ptr: Exclusive Ownership

One owner, automatic cleanup:
```cpp
#include <memory>

auto ptr = std::make_unique<int>(42);  // Preferred creation
std::unique_ptr<int> ptr2(new int(42)); // Alternative

// Cannot copy, only move
auto ptr3 = std::move(ptr);  // ptr is now null
```

### std::shared_ptr: Shared Ownership

Multiple owners, reference counted:
```cpp
auto ptr1 = std::make_shared<int>(42);
auto ptr2 = ptr1;  // Both own the object
// Reference count = 2

ptr1.reset();  // Reference count = 1
// Object deleted when ptr2 goes out of scope
```

### std::weak_ptr: Breaking Cycles

Non-owning reference to shared object:
```cpp
std::weak_ptr<int> weak = shared;

if (auto locked = weak.lock()) {
    // Object still exists, locked is a shared_ptr
    use(*locked);
}
```

### Rule of Three (or Rule of Zero)

If you define any of: destructor, copy constructor, copy assignment,
you should define all three.

Better: Rule of Zero - use smart pointers and let compiler generate defaults.

### Passing Smart Pointers

```cpp
void take_ownership(std::unique_ptr<Widget> w);  // Takes ownership
void share_ownership(std::shared_ptr<Widget> w); // Shares ownership
void just_use(Widget& w);                        // No ownership change
```

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Use `unique_ptr` by default for heap objects
2. Use `shared_ptr` only when ownership is truly shared
3. Use `weak_ptr` to break cycles
4. Prefer `make_unique`/`make_shared`

## Next Steps

Proceed to [Day 10: RAII, Move Semantics, and Destructors](../day-10/README.md).
