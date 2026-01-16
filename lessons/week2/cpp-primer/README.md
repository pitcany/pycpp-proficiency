# 🔧 Day 7.5: C++ Primer for Absolute Beginners

**Language**: C++
**Time Estimate**: 3-4 hours
**Notion Source**: [Link](https://www.notion.so/025d4011a8d34710a6dc71d362a7a987)

## Purpose

This optional half-day module bridges Week 1 (Python) and Week 2 (C++) for learners with **zero prior C++ experience**. If you've never written C++ before, complete this section before starting Day 8.

### Who should do this:

- You have never compiled or run a C++ program
- You don't know what `int main()` does
- You're unfamiliar with C++ syntax (even if you know Python well)

### Who can skip this:

- You've taken an intro C++ course or tutorial
- You can write basic C++ programs (variables, loops, functions) and compile them
- You're comfortable reading simple C++ code

## Learning Objectives

By the end of Day 7.5, you will be able to:

- [ ] Compile and run a simple C++ program
- [ ] Declare variables with proper types
- [ ] Write functions that take parameters and return values
- [ ] Use basic control flow (if/else, for loops, while loops)
- [ ] Understand what `#include`, `std::`, and `main()` mean
- [ ] Read compiler error messages without panic

## Setup Verification

Before starting, verify your C++ environment is working:

### Step 1: Create a test file

Create a file named `hello.cpp`:
```cpp
#include <iostream>

int main() {
    std::cout << "Hello from C++!" << std::endl;
    return 0;
}
```

### Step 2: Compile and run

**On macOS/Linux:**
```bash
g++ -std=c++17 hello.cpp -o hello
./hello
```

**On Windows (with MinGW or MSVC):**
```bash
g++ -std=c++17 hello.cpp -o hello.exe
hello.exe
```

If you see `Hello from C++!`, your environment is ready. If not, revisit the setup instructions from Day 0.

## Core Concepts

See [cpp/concepts.md](cpp/concepts.md) for detailed explanations of:
- Program structure and `main()`
- Variables and explicit types
- Functions with type declarations
- Control flow (if/else, loops)
- Arrays and vectors
- Understanding `std::` namespace
- Compilation basics

## Compilation Basics

### What happens when you compile?

1. **Preprocessing:** `#include` statements are expanded
2. **Compilation:** C++ code is translated to machine code
3. **Linking:** Multiple files and libraries are combined
4. **Executable:** You get a runnable program

### Common compiler flags

```bash
g++ -std=c++17 -Wall -Wextra -o myprogram myprogram.cpp
```

- `-std=c++17`: Use C++17 standard (modern features)
- `-Wall -Wextra`: Enable helpful warnings
- `-o myprogram`: Name the output executable

## Exercises

See [exercises.md](exercises.md) for practice problems.

## Self-Assessment Checklist

Before proceeding to Day 8, verify you can:

- [ ] Compile and run a C++ program without errors
- [ ] Declare variables with appropriate types (`int`, `double`, `bool`)
- [ ] Write a function that takes parameters and returns a value
- [ ] Use `std::vector` to store a collection of values
- [ ] Write a for loop to iterate through a vector
- [ ] Use `std::cout` to print results
- [ ] Read a compiler error message and identify the line number
- [ ] Explain the difference between `#include`, `main()`, and `return 0;`

**If you can complete this checklist, you're ready for Day 8.**

## Key Takeaways

1. C++ requires explicit type declarations (unlike Python)
2. Every program starts with `int main()`
3. Compilation is a separate step from running
4. Semicolons are required at the end of statements
5. Use `std::vector` instead of C-style arrays

## Reading Compiler Errors

Compiler errors can be intimidating. Focus on:

1. **File and line number** (e.g., `myprogram.cpp:10:5`)
2. **First error message** (later errors often cascade from the first)
3. **Key phrases**: "expected ';'", "undeclared identifier", "type mismatch"

**Common beginner errors:**
- Missing semicolon: `error: expected ';' before 'return'`
- Undeclared variable: `error: 'x' was not declared in this scope`
- Type mismatch: `error: cannot convert 'double' to 'int'`

## Additional Resources

If you need more help:
- [LearnCpp.com](http://LearnCpp.com) (Chapters 1-6)
- [C++ Tutorial for Beginners](https://www.youtube.com/watch?v=vLnPwxZdW4Y) (first 2 hours)

## What You're NOT Learning Here

This primer covers only the bare minimum. You will NOT learn:

- Object-oriented programming (classes, inheritance)
- Templates or generic programming
- Memory management (pointers, `new`/`delete`) → **Day 8 covers this**
- Standard library algorithms → **Day 11 covers this**
- Performance optimization → **Days 13-14 cover this**

These topics are covered in Week 2. Day 7.5 just ensures you can read and write basic C++ syntax before diving into the advanced topics needed for statistical computing.

## Estimated Time

- **Reading concepts:** 1.5 hours
- **Setup verification:** 30 min
- **Exercises:** 1 hour
- **Self-assessment:** 30 min
- **Total:** 3-4 hours

**If you spend more than 6 hours on Day 7.5**, consider working through a full beginner C++ tutorial before continuing. The curriculum assumes you can pick up basic syntax quickly because you already know Python.

## Next Steps

Once you've completed the self-assessment checklist, proceed to [Week 2: C++ (Days 8-14)](../day-08/README.md), starting with Day 8: References, Pointers, and Ownership.
