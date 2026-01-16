# Day 8: References, Pointers, and Ownership

**Language**: C++
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/48da4fa9d9b4495698ebe27a66a92de5)

> **Note for absolute beginners**: If you have never written C++ before, complete [Day 7.5: C++ Primer](../cpp-primer/README.md) before starting this lesson.

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Distinguish between references and pointers
- [ ] Use pass-by-reference correctly for function parameters
- [ ] Understand stack vs heap allocation
- [ ] Reason about object lifetime and ownership
- [ ] Avoid dangling pointers and references
- [ ] Use smart pointers for automatic memory management

## Sections

### Pointers vs References

Key differences:
```cpp
int x = 42;
int* ptr = &x;   // Pointer: can be null, can be reassigned
int& ref = x;    // Reference: cannot be null, cannot be reassigned

*ptr = 10;       // Dereference pointer
ref = 10;        // Reference used directly
```

### Pass by Value vs Reference vs Pointer

```cpp
void by_value(int x);          // Copy
void by_ref(int& x);           // Can modify original
void by_const_ref(const int& x);  // Read-only, no copy
void by_ptr(int* x);           // Nullable, can modify
```

### Ownership: Who is Responsible for Cleanup?

The fundamental question in C++: Who owns this memory?
- Stack objects: automatic cleanup
- Heap objects: manual or smart pointer cleanup

### Dangling Pointers and References

```cpp
// DANGER: Returning reference to local
int& bad() {
    int local = 42;
    return local;  // local dies when function returns!
}

// DANGER: Dangling pointer
int* also_bad() {
    int local = 42;
    return &local;  // Same problem
}
```

### Stack vs Heap Allocation

```cpp
void stack_example() {
    int x = 42;        // Stack: fast, automatic cleanup
    int arr[100];      // Stack: fixed size
}  // Everything cleaned up here

void heap_example() {
    int* p = new int(42);   // Heap: manual cleanup needed
    int* arr = new int[n];  // Heap: dynamic size
    delete p;               // Must delete!
    delete[] arr;           // Must use delete[] for arrays
}
```

### Build Systems and Debugging

Setting up CMake and AddressSanitizer.

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. Prefer references over pointers when possible
2. Use `const&` for read-only parameters
3. Stack allocation is fast and safe
4. Every `new` needs a `delete` (or use smart pointers)

## Next Steps

Proceed to [Day 9: Smart Pointers and Ownership Semantics](../day-09/README.md).
