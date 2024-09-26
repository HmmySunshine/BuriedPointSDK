# coding=utf-8
import shutil
import os
import sys
import argparse



# 获取脚本所在路径
SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0]
# 获取构建目录路径
BUILD_DIR_PATH = SCRIPT_PATH + '/../build'


# 清空构建目录
def clear():
    if os.path.exists(BUILD_DIR_PATH):
        shutil.rmtree(BUILD_DIR_PATH)


# 构建windows平台
def build_windows(platform='x64', config='Release', args=None):
    
    # 获取构建目录路径
    platform_dir = '%s/%s-%s' % (BUILD_DIR_PATH, platform, config)
    # 创建构建目录
    os.makedirs(platform_dir, exist_ok=True)

    # 切换到构建目录
    os.chdir(platform_dir)

   
    # 构建命令
    build_cmd = 'cmake ../.. -G "Visual Studio 17 2022" -DCMAKE_BUILD_TYPE=%s -DCMAKE_GENERATOR_PLATFORM=%s -T v143' % (
        config, platform)
   
    # 如果需要运行测试，添加测试选项
    if args.test:
        build_cmd += ' -DBUILD_BURIED_TEST=ON'

    # 如果需要运行示例，添加示例选项
    if args.example:
        build_cmd += ' -DBUILD_BURIED_EXAMPLES=ON'

    # 打印构建命令
    print("build cmd:" + build_cmd)
    
    # 执行构建命令
    ret = os.system(build_cmd)
    # 如果构建失败，打印错误信息
    if ret != 0:
        print('!!!!!!!!!!!!!!!!!!build fail')
        return False
   
    # 构建命令
    build_cmd = 'cmake --build . --config %s --parallel 8' % (config)
    # 执行构建命令
    ret = os.system(build_cmd)
    # 如果构建失败，打印错误信息
    if ret != 0:
        print('build fail!!!!!!!!!!!!!!!!!!!!')
        return False
    return True


# 主函数
def main():
    # 清空构建目录
    clear()
    # 创建构建目录
    os.makedirs(BUILD_DIR_PATH, exist_ok=True)
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='build windows')
    # 添加测试选项
    parser.add_argument('--test', action='store_true', default=False,
                        help='run unittest')
    # 添加示例选项
    parser.add_argument('--example', action='store_true', default=False,
                        help='run examples')
    # 解析命令行参数
    args = parser.parse_args()

    # 构建windows平台
    if not build_windows(platform='x64', config='Debug', args=args):
        exit(1)


if __name__ == '__main__':
    main()