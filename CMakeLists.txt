cmake_minimum_required(VERSION 3.16)
project(pycpp_proficiency
    VERSION 1.0.0
    DESCRIPTION "C++ components for Python & C++ Proficiency course"
    LANGUAGES CXX
)

# C++ Standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Build type defaults
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Compiler warnings
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(
        -Wall
        -Wextra
        -Wpedantic
        -Werror=return-type
    )
endif()

# Sanitizers for Debug builds
option(ENABLE_SANITIZERS "Enable AddressSanitizer and UBSan in Debug builds" ON)
if(ENABLE_SANITIZERS AND CMAKE_BUILD_TYPE STREQUAL "Debug")
    add_compile_options(-fsanitize=address,undefined -fno-omit-frame-pointer)
    add_link_options(-fsanitize=address,undefined)
endif()

# Include shared library
add_subdirectory(src/cpp_lib)

# Optional: pybind11 bindings
option(BUILD_PYTHON_BINDINGS "Build Python bindings with pybind11" OFF)
if(BUILD_PYTHON_BINDINGS)
    find_package(pybind11 CONFIG)
    if(pybind11_FOUND)
        message(STATUS "Building Python bindings")
        # Add binding targets here
    else()
        message(WARNING "pybind11 not found, skipping Python bindings")
    endif()
endif()

# Tests
option(BUILD_TESTS "Build unit tests" ON)
if(BUILD_TESTS)
    enable_testing()
    find_package(GTest CONFIG)
    if(GTest_FOUND)
        add_subdirectory(tests/cpp)
    else()
        message(STATUS "GoogleTest not found, skipping C++ tests")
    endif()
endif()

# Demo executable
add_executable(demo
    ${CMAKE_CURRENT_SOURCE_DIR}/benchmarks/cpp/demo.cpp
)
target_link_libraries(demo PRIVATE cpp_lib)

# Install targets
install(TARGETS demo DESTINATION bin)
install(DIRECTORY src/cpp_lib/include/ DESTINATION include)

# Print configuration summary
message(STATUS "")
message(STATUS "=== pycpp_proficiency Configuration ===")
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Sanitizers: ${ENABLE_SANITIZERS}")
message(STATUS "Python bindings: ${BUILD_PYTHON_BINDINGS}")
message(STATUS "Tests: ${BUILD_TESTS}")
message(STATUS "========================================")
