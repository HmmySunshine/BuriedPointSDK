# 设置最低的CMake版本要求
cmake_minimum_required(VERSION 3.20)

# 设置项目名称
set(PROJECT_NAME "BuriedPoint")

# 创建项目
project(${PROJECT_NAME} VERSION 1.1.1.1)

# 设置编译选项
option(BUILD_BURIED_SHARED_LIBS "build shared library" ON)
option(BUILD_BURIED_STATIC_LIBS "build static library" ON)

option(BUILD_BURIED_EXAMPLES "build examples" OFF)
option(BUILD_BURIED_TEST "build unittest" OFF)

option(BUILD_BURIED_FOR_MT "build for /MT" OFF)

# 设置编译器标志
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /MP")

# 如果为/MT编译，设置编译器标志
if(BUILD_BURIED_FOR_MT)
    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} /MTd")
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")
    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /MT")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")
endif()

# 设置需要链接的库
set(LIBS ${LIBS} winmm iphlpapi ws2_32 dbghelp)

# 生成pdb文件
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /Zi")
set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /Zi")
set(CMAKE_SHARED_LINKER_FLAGS_RELEASE
    "${CMAKE_EXE_LINKER_FLAGS_RELEASE} /DEBUG /OPT:REF /OPT:ICF")

# 设置包含目录
set(INCDIRS . lib ${CMAKE_BINARY_DIR})
include_directories(${INCDIRS})

# 设置编译器标准
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /std:c++20")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /std:c11")

# 输出CMake配置信息
message(STATUS "CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}")
message(STATUS "CMAKE_SYSTEM_NAME=${CMAKE_SYSTEM_NAME}")

# 根据编译类型设置宏定义
if("${CMAKE_BUILD_TYPE}" STREQUAL "Debug")
    add_definitions(-DDEBUG)
else()
    add_definitions(-DNDEBUG)
endif()

# 添加子目录
add_subdirectory(src)

# 如果需要构建示例，添加子目录
if(BUILD_BURIED_EXAMPLES)
    add_subdirectory(examples)
endif()

# 如果需要构建测试，添加子目录
if(BUILD_BURIED_TEST)
    include_directories(
        googletest/googletest
        googletest/googletest/include)
    add_subdirectory(googletest)
    add_subdirectory(tests)
endif()