# 包含全局变量
include_guard(GLOBAL)
include_directories(. third_party/spdlog-1.12.0/include)
include_directories(. third_party/mbedtls/include)
include_directories(. third_party/boost)
#不要加boostjson
add_definitions(-DBOOST_JSON_NO_LIB)

#不定义这个宏会造成自定义格式化异常 日志格式化异常
add_definitions(-DSPDLOG_ACTIVE_LEVEL=SPDLOG_LEVEL_TRACE)
#
# 添加spdlog-1.12.0子目录
add_subdirectory(third_party/spdlog-1.12.0)
# 添加mbedtls/library子目录
add_subdirectory(third_party/mbedtls/library)

# 设置源文件
set(BURIED_SRCS buried.cc)

# 设置模块名称
set(MODULE_NAME "Buried")

# 打印libs变量
message(STATUS "libs ${LIBS}")


# 如果构建Buried共享库
if(BUILD_BURIED_SHARED_LIBS)
    # 添加共享库
    add_library(${MODULE_NAME} SHARED ${BURIED_SRCS})
    # 链接库
    target_link_libraries(${MODULE_NAME} PRIVATE ${LIBS} spdlog mbedtls_static)
endif()


# 如果构建Buried静态库
if(BUILD_BURIED_STATIC_LIBS)
    # 添加静态库
    add_library(${MODULE_NAME}_static STATIC ${BURIED_SRCS})
    # 链接库
    target_link_libraries(${MODULE_NAME} PRIVATE ${LIBS} spdlog mbedtls_static)
endif()