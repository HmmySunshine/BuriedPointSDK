# 设置CMake的最低版本要求
cmake_minimum_required(VERSION 3.20)
# 设置测试源文件
set(TEST_SRC
	test.cc)
# 添加可执行文件
add_executable(buried_test ${TEST_SRC})
# 链接库
target_link_libraries(buried_test Buried_static gtest)