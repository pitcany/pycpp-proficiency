# C++ library for course utilities
cmake_minimum_required(VERSION 3.16)

# Header-only library
add_library(cpp_lib INTERFACE)
target_include_directories(cpp_lib INTERFACE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
target_compile_features(cpp_lib INTERFACE cxx_std_17)
