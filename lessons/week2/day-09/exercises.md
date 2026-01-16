# Day 9: Smart Pointers and Ownership Semantics - Exercises

## Foundational Exercises

### Exercise 9.1: Implement Rule of Three

**Objective**: Implement a class following the Rule of Three.

```cpp
#include <cstring>
#include <iostream>

class String {
private:
    char* data_;
    size_t length_;

public:
    // Constructor
    String(const char* str = "") {
        length_ = std::strlen(str);
        data_ = new char[length_ + 1];
        std::strcpy(data_, str);
    }

    // TODO: Implement destructor
    ~String() {
        // Free allocated memory
    }

    // TODO: Implement copy constructor
    String(const String& other) {
        // Deep copy
    }

    // TODO: Implement copy assignment operator
    String& operator=(const String& other) {
        // Handle self-assignment, deep copy
    }

    const char* c_str() const { return data_; }
    size_t length() const { return length_; }
};

// Test
int main() {
    String s1("Hello");
    String s2 = s1;        // Copy constructor
    String s3;
    s3 = s1;               // Copy assignment

    std::cout << s1.c_str() << std::endl;
    std::cout << s2.c_str() << std::endl;
    std::cout << s3.c_str() << std::endl;

    return 0;
}
```

---

### Exercise 9.2: Break Reference Cycle

**Objective**: Fix a memory leak caused by circular references.

```cpp
#include <memory>
#include <iostream>

class Node {
public:
    std::shared_ptr<Node> next;  // Bug: creates cycle
    std::shared_ptr<Node> prev;  // Bug: creates cycle

    ~Node() {
        std::cout << "Node destroyed" << std::endl;
    }
};

int main() {
    auto node1 = std::make_shared<Node>();
    auto node2 = std::make_shared<Node>();

    node1->next = node2;
    node2->prev = node1;  // Circular reference!

    // node1 and node2 never get destroyed due to cycle
    return 0;
}

// TODO: Fix using weak_ptr
```

---

### Exercise 9.3: unique_ptr Factory

**Objective**: Implement factory functions returning unique_ptr.

```cpp
#include <memory>
#include <string>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
    virtual std::string name() const = 0;
};

class Circle : public Shape {
    double radius_;
public:
    Circle(double r) : radius_(r) {}
    double area() const override { return 3.14159 * radius_ * radius_; }
    std::string name() const override { return "Circle"; }
};

class Rectangle : public Shape {
    double width_, height_;
public:
    Rectangle(double w, double h) : width_(w), height_(h) {}
    double area() const override { return width_ * height_; }
    std::string name() const override { return "Rectangle"; }
};

// TODO: Implement factory function
std::unique_ptr<Shape> create_shape(const std::string& type, double a, double b = 0) {
    // Return appropriate shape based on type
    // "circle" -> Circle(a)
    // "rectangle" -> Rectangle(a, b)
    // unknown -> nullptr
}

// Test
int main() {
    auto circle = create_shape("circle", 5.0);
    auto rect = create_shape("rectangle", 3.0, 4.0);

    if (circle) {
        std::cout << circle->name() << " area: " << circle->area() << std::endl;
    }
    if (rect) {
        std::cout << rect->name() << " area: " << rect->area() << std::endl;
    }

    return 0;
}
```

---

## Proficiency Exercises

### Exercise 9.4: Smart Pointer Ownership

**Objective**: Choose correct smart pointer types for a class hierarchy.

```cpp
#include <memory>
#include <vector>

class Observer;  // Forward declaration

class Subject {
    // TODO: What type for observers?
    // They should not extend Subject's lifetime
    ??? observers_;

public:
    void attach(???);
    void detach(???);
    void notify();
};

class Observer {
    // TODO: What type for subject?
    // Observer needs access but doesn't own Subject
    ??? subject_;

public:
    void set_subject(???);
    void on_notify();
};

class ResourceManager {
    // TODO: What type for resources?
    // Manager exclusively owns resources
    ??? resources_;

public:
    void add_resource(???);
    ??? get_resource(size_t index);
};
```

---

### Exercise 9.5: Custom Deleter

**Objective**: Use unique_ptr with a custom deleter.

```cpp
#include <memory>
#include <cstdio>

// FILE* needs fclose, not delete
// Use unique_ptr with custom deleter

// TODO: Create type alias for FILE* unique_ptr
// using FilePtr = ???

FilePtr open_file(const char* path, const char* mode) {
    // TODO: Return unique_ptr that will call fclose
}

int main() {
    auto file = open_file("test.txt", "w");
    if (file) {
        fprintf(file.get(), "Hello, World!\n");
    }
    // File automatically closed when file goes out of scope
    return 0;
}
```

---

## Mastery Exercises

### Exercise 9.6: Implement shared_ptr

**Objective**: Implement a simplified shared_ptr.

```cpp
template<typename T>
class SharedPtr {
private:
    T* ptr_;
    int* ref_count_;

public:
    // Default constructor
    SharedPtr() : ptr_(nullptr), ref_count_(nullptr) {}

    // Constructor from raw pointer
    explicit SharedPtr(T* ptr) {
        // TODO: Initialize ptr_ and ref_count_
    }

    // Copy constructor
    SharedPtr(const SharedPtr& other) {
        // TODO: Share ownership, increment count
    }

    // Copy assignment
    SharedPtr& operator=(const SharedPtr& other) {
        // TODO: Handle self-assignment, share ownership
    }

    // Destructor
    ~SharedPtr() {
        // TODO: Decrement count, delete if zero
    }

    T* get() const { return ptr_; }
    T& operator*() const { return *ptr_; }
    T* operator->() const { return ptr_; }
    int use_count() const { return ref_count_ ? *ref_count_ : 0; }

private:
    void release() {
        // TODO: Decrement count, delete if zero
    }
};
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Rule of Three | Incomplete | Has bugs | Correct |
| Cycle detection | Cannot identify | Identifies | Fixes correctly |
| Smart pointer choice | Wrong types | Mostly correct | All optimal |
| Custom deleters | Cannot implement | Basic usage | Advanced usage |
