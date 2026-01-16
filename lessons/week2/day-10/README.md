# Day 10: RAII, Move Semantics, and Destructors

**Language**: C++
**Time Estimate**: 6-8 hours
**Notion Source**: [Link](https://www.notion.so/c5185fd171504ab7a9cbc3144072c5ca)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Understand the RAII principle and philosophy
- [ ] Use unique_ptr for automatic cleanup
- [ ] Recognize when destructors run
- [ ] Write RAII wrappers for custom resources
- [ ] Understand exception safety through RAII

## Sections

### RAII: Resource Acquisition Is Initialization

Core principle: Bind resource lifetime to object lifetime.
- Acquire resources in constructor
- Release resources in destructor
- Object scope determines resource lifetime

```cpp
class File {
    FILE* file_;
public:
    File(const char* path) : file_(fopen(path, "r")) {
        if (!file_) throw std::runtime_error("Cannot open file");
    }
    ~File() { if (file_) fclose(file_); }

    // Prevent copying
    File(const File&) = delete;
    File& operator=(const File&) = delete;
};
```

### Common RAII Types

Standard library RAII wrappers:
- `std::unique_ptr`, `std::shared_ptr` - memory
- `std::lock_guard`, `std::unique_lock` - mutexes
- `std::fstream` - files
- `std::vector`, `std::string` - dynamic memory

### Writing RAII Wrappers

Pattern for wrapping C resources:
```cpp
template<typename T, auto Deleter>
class RAIIWrapper {
    T resource_;
public:
    explicit RAIIWrapper(T r) : resource_(r) {}
    ~RAIIWrapper() { if (resource_) Deleter(resource_); }

    T get() const { return resource_; }
    T release() { T r = resource_; resource_ = {}; return r; }

    // Non-copyable
    RAIIWrapper(const RAIIWrapper&) = delete;
    RAIIWrapper& operator=(const RAIIWrapper&) = delete;
};
```

### Destructors: Cleanup Guarantees

Destructors run:
- When stack objects go out of scope
- When `delete` is called on heap objects
- When smart pointers release ownership
- During stack unwinding (exceptions)

### Exception Safety and RAII

RAII provides exception safety for free:
```cpp
void safe_function() {
    auto resource = std::make_unique<Resource>();
    may_throw();  // Even if this throws, resource is cleaned up
}
```

### The Rule of Zero

Best practice: Let compiler generate special members.
```cpp
class Modern {
    std::unique_ptr<Data> data_;
    std::string name_;
public:
    // Compiler generates correct destructor, copy, move
};
```

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Key Takeaways

1. RAII = resource lifetime tied to object lifetime
2. Destructors provide cleanup guarantees
3. RAII provides exception safety
4. Prefer Rule of Zero with smart pointers

## Next Steps

Proceed to [Day 11: STL Containers, Algorithms, and Iterators](../day-11/README.md).
