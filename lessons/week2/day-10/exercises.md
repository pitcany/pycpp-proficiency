# Day 10: RAII, Move Semantics, and Destructors - Exercises

## Foundational Exercises

### Exercise 10.1: RAII File Wrapper

**Objective**: Implement a RAII wrapper for C file operations.

```cpp
#include <cstdio>
#include <stdexcept>
#include <string>

class FileHandle {
private:
    FILE* file_;

public:
    // Constructor: opens file
    FileHandle(const std::string& path, const std::string& mode) {
        // TODO: Open file, throw if fails
    }

    // Destructor: closes file
    ~FileHandle() {
        // TODO: Close file if open
    }

    // Delete copy operations
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;

    // Implement move operations
    FileHandle(FileHandle&& other) noexcept {
        // TODO: Take ownership from other
    }

    FileHandle& operator=(FileHandle&& other) noexcept {
        // TODO: Close current, take ownership from other
    }

    // Access methods
    FILE* get() const { return file_; }
    bool is_open() const { return file_ != nullptr; }

    // Read entire file as string
    std::string read_all() {
        // TODO: Read and return file contents
    }
};

// Test
int main() {
    try {
        FileHandle file("test.txt", "w");
        fprintf(file.get(), "Hello, RAII!\n");
    }  // File automatically closed

    {
        FileHandle file("test.txt", "r");
        auto content = file.read_all();
        printf("Read: %s", content.c_str());
    }

    return 0;
}
```

---

### Exercise 10.2: Scoped Timer

**Objective**: Implement a RAII timer for performance measurement.

```cpp
#include <chrono>
#include <iostream>
#include <string>

class ScopedTimer {
private:
    std::string name_;
    std::chrono::high_resolution_clock::time_point start_;

public:
    explicit ScopedTimer(const std::string& name)
        : name_(name), start_(std::chrono::high_resolution_clock::now()) {
        // TODO: Record start time
    }

    ~ScopedTimer() {
        // TODO: Calculate elapsed time and print
        // Format: "Timer [name]: X.XXX ms"
    }

    // Non-copyable, non-movable
    ScopedTimer(const ScopedTimer&) = delete;
    ScopedTimer& operator=(const ScopedTimer&) = delete;
};

// Usage macro for convenient timing
#define TIMED_SCOPE(name) ScopedTimer _timer_##__LINE__(name)

// Test
void slow_function() {
    TIMED_SCOPE("slow_function");
    // Simulate work
    volatile int sum = 0;
    for (int i = 0; i < 1000000; ++i) {
        sum += i;
    }
}

int main() {
    {
        ScopedTimer timer("whole program");
        slow_function();
        slow_function();
    }
    return 0;
}
```

---

### Exercise 10.3: Exception Safety with RAII

**Objective**: Compare exception safety with and without RAII.

```cpp
#include <memory>
#include <stdexcept>
#include <iostream>

class Resource {
public:
    Resource() { std::cout << "Resource acquired\n"; }
    ~Resource() { std::cout << "Resource released\n"; }
    void use() { std::cout << "Resource used\n"; }
};

// Bad: Not exception safe
void unsafe_version() {
    Resource* r1 = new Resource();
    Resource* r2 = new Resource();

    try {
        r1->use();
        throw std::runtime_error("Error!");  // r1 and r2 leak!
        r2->use();
    } catch (...) {
        delete r1;  // We might forget this
        delete r2;  // Or this
        throw;
    }

    delete r1;
    delete r2;
}

// TODO: Implement safe version using RAII
void safe_version() {
    // Use unique_ptr to ensure cleanup even if exception thrown
}

int main() {
    std::cout << "=== Unsafe version ===" << std::endl;
    try {
        unsafe_version();
    } catch (const std::exception& e) {
        std::cout << "Caught: " << e.what() << std::endl;
    }

    std::cout << "\n=== Safe version ===" << std::endl;
    try {
        safe_version();
    } catch (const std::exception& e) {
        std::cout << "Caught: " << e.what() << std::endl;
    }

    return 0;
}
```

---

## Proficiency Exercises

### Exercise 10.4: Lock Guard Implementation

**Objective**: Implement a simple lock guard for mutex locking.

```cpp
#include <mutex>
#include <iostream>
#include <thread>
#include <vector>

template<typename Mutex>
class LockGuard {
private:
    Mutex& mutex_;

public:
    explicit LockGuard(Mutex& m) : mutex_(m) {
        // TODO: Lock the mutex
    }

    ~LockGuard() {
        // TODO: Unlock the mutex
    }

    // Non-copyable, non-movable
    LockGuard(const LockGuard&) = delete;
    LockGuard& operator=(const LockGuard&) = delete;
};

// Test with multiple threads
std::mutex mtx;
int counter = 0;

void increment() {
    for (int i = 0; i < 1000; ++i) {
        LockGuard<std::mutex> lock(mtx);
        ++counter;
    }
}

int main() {
    std::vector<std::thread> threads;
    for (int i = 0; i < 10; ++i) {
        threads.emplace_back(increment);
    }
    for (auto& t : threads) {
        t.join();
    }
    std::cout << "Counter: " << counter << " (expected: 10000)" << std::endl;
    return 0;
}
```

---

### Exercise 10.5: RAII Database Connection

**Objective**: Create a RAII wrapper for a mock database connection.

```cpp
#include <iostream>
#include <stdexcept>
#include <string>

// Mock database API (simulates C-style interface)
struct DBConnection {
    bool connected = false;
    std::string db_name;
};

DBConnection* db_connect(const char* name) {
    std::cout << "Connecting to " << name << std::endl;
    auto conn = new DBConnection();
    conn->connected = true;
    conn->db_name = name;
    return conn;
}

void db_disconnect(DBConnection* conn) {
    if (conn && conn->connected) {
        std::cout << "Disconnecting from " << conn->db_name << std::endl;
        conn->connected = false;
    }
    delete conn;
}

bool db_query(DBConnection* conn, const char* sql) {
    if (!conn || !conn->connected) return false;
    std::cout << "Executing: " << sql << std::endl;
    return true;
}

// TODO: Implement RAII wrapper
class Database {
    // Your implementation here
};

int main() {
    try {
        Database db("mydb");
        db.query("SELECT * FROM users");
        db.query("INSERT INTO logs VALUES (1, 'test')");
        throw std::runtime_error("Simulated error");
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    // Connection should be closed automatically

    return 0;
}
```

---

## Mastery Exercises

### Exercise 10.6: Move Semantics

**Objective**: Implement a class with proper move semantics.

```cpp
#include <algorithm>
#include <iostream>

class Buffer {
private:
    double* data_;
    size_t size_;

public:
    // Constructor
    explicit Buffer(size_t size) : size_(size) {
        data_ = new double[size];
        std::fill(data_, data_ + size, 0.0);
        std::cout << "Constructed buffer of size " << size << std::endl;
    }

    // Destructor
    ~Buffer() {
        delete[] data_;
        std::cout << "Destroyed buffer" << std::endl;
    }

    // TODO: Copy constructor (deep copy)
    Buffer(const Buffer& other) {
    }

    // TODO: Copy assignment (deep copy)
    Buffer& operator=(const Buffer& other) {
    }

    // TODO: Move constructor
    Buffer(Buffer&& other) noexcept {
    }

    // TODO: Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
    }

    double& operator[](size_t i) { return data_[i]; }
    size_t size() const { return size_; }
};

Buffer create_buffer(size_t size) {
    Buffer b(size);
    b[0] = 42.0;
    return b;  // Move should happen here
}

int main() {
    std::cout << "=== Creating buffer ===" << std::endl;
    Buffer b1(10);
    b1[0] = 1.0;

    std::cout << "\n=== Copy construction ===" << std::endl;
    Buffer b2 = b1;  // Copy

    std::cout << "\n=== Move construction ===" << std::endl;
    Buffer b3 = std::move(b1);  // Move

    std::cout << "\n=== Factory function ===" << std::endl;
    Buffer b4 = create_buffer(5);  // Move (or RVO)

    std::cout << "\n=== End of main ===" << std::endl;
    return 0;
}
```

---

## Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| RAII pattern | Not followed | Partial | Complete |
| Exception safety | Leaks on exception | Basic safety | Strong guarantee |
| Move semantics | Not implemented | Has bugs | Correct |
| Resource cleanup | Missing cleanup | Manual cleanup | Automatic RAII |
