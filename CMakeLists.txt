
# 设置CMake最低版本要求
cmake_minimum_required(VERSION 3.20)


# 设置项目名称
set(PROJECT_NAME "BuriedPoint")


# 创建项目
project(${PROJECT_NAME} VERSION 1.1.1.1)


# 设置选项，是否构建共享库
option(BUILD_BURIED_SHARED_LIBS "build shared library" ON)
# 设置选项，是否构建静态库
option(BUILD_BURIED_STATIC_LIBS "build static library" ON)

# 设置选项，是否构建示例
option(BUILD_BURIED_EXAMPLES "build examples" OFF)
# 设置选项，是否构建单元测试
option(BUILD_BURIED_TEST "build unittest" OFF)

# 设置选项，是否构建/MT版本
option(BUILD_BURIED_FOR_MT "build for /MT" OFF)

# 设置C++编译选项，多线程编译
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /MP")


# 如果构建/MT版本，设置C和C++编译选项
if(BUILD_BURIED_FOR_MT)
    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} /MTd")
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")
    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /MT")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")
endif()


# 设置需要链接的库
set(LIBS ${LIBS} winmm iphlpapi ws2_32 dbghelp)


# 设置C++编译选项，调试信息
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /Zi")
# 设置C编译选项，调试信息
set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /Zi")
# 设置共享链接选项，调试信息
set(CMAKE_SHARED_LINKER_FLAGS_RELEASE
    "${CMAKE_EXE_LINKER_FLAGS_RELEASE} /DEBUG /OPT:REF /OPT:ICF")


# 设置包含目录
set(INCDIRS . lib ${CMAKE_BINARY_DIR})
include_directories(${INCDIRS})


# 设置C++编译选项，C++20标准
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /std:c++20")
# 设置C编译选项，C11标准
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /std:c11")


# 输出构建类型和系统名称
message(STATUS "CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}")
message(STATUS "CMAKE_SYSTEM_NAME=${CMAKE_SYSTEM_NAME}")

# 如果构建类型为Debug，添加DEBUG定义；否则添加NDEBUG定义
if("${CMAKE_BUILD_TYPE}" STREQUAL "Debug")
    add_definitions(-DDEBUG)
else()
    add_definitions(-DNDEBUG)
endif()


# 添加子目录src
add_subdirectory(src)


# 如果构建示例，添加子目录examples
if(BUILD_BURIED_EXAMPLES)
    add_subdirectory(examples)
endif()


# 如果构建单元测试，添加子目录googletest和tests
if(BUILD_BURIED_TEST)
    include_directories(
        googletest/googletest
        googletest/googletest/include)
    add_subdirectory(googletest)
    add_subdirectory(tests)
endif()