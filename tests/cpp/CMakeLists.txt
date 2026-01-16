# C++ tests using GoogleTest

add_executable(test_numerical test_numerical.cpp)
target_link_libraries(test_numerical PRIVATE cpp_lib GTest::gtest_main)

add_executable(test_stats test_stats.cpp)
target_link_libraries(test_stats PRIVATE cpp_lib GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(test_numerical)
gtest_discover_tests(test_stats)
