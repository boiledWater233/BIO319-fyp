#!/usr/bin/env python3
"""
BioMethodExtractor - 安装与配置脚本

使用方法: python install.py
"""

import os
import sys
import subprocess
import json
from pathlib import Path

# ==========================================
# 配置常量
# ==========================================
REQUIRED_PYTHON_VERSION = (3, 8)
ENV_FILE = ".env"
CONFIG_FILE = "config.json"
DEFAULT_OUTPUT_DIR = "output"
TEST_DATA_DIR = "tests/data"


# ==========================================
# 检查函数
# ==========================================
def check_python_version():
    """检查 Python 版本"""
    print("[1/7] python version")
    current_version = sys.version_info[:2]

    if current_version >= REQUIRED_PYTHON_VERSION:
        print(f"    + Python >={current_version[0]}.{current_version[1]} ")
        return True
    else:
        print(f"    - Python version too low {'.'.join(map(str, REQUIRED_PYTHON_VERSION))}+")
        return False





# ==========================================
# 安装函数
# ==========================================
def install_dependencies():
    """安装依赖库"""
    print("installing package")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--upgrade"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("    + installed")
            return True
        else:
            print(f"    - failed: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"    - ERR:{str(e)}")
        return False


# ==========================================
# 配置函数
# ==========================================
def setup_api_key():
    """配置 API Key"""
    print("API Key...")
    print(" API Key will saved at .env file")

    api_key = input(" Set api key (Start with sk-... or local model): ").strip()

    if api_key:
        with open(ENV_FILE, 'w', encoding='utf-8') as f:
            f.write(f"DEEPSEEK_API_KEY={api_key}\n")
        print("    ✓ API Key saved")
    else:
        print("    ⚠ 跳过配置，请手动创建 .env 文件")
        with open(f"{ENV_FILE}.example", 'w', encoding='utf-8') as f:
            f.write("DEEPSEEK_API_KEY=sk-your-key-here\n")
        print(f"    ✓ 已创建示例文件：{ENV_FILE}.example")


def setup_default_input():
    """配置默认输入文件"""
    print("[5/7] default input")

    default_file = input("    default pdf input file: ").strip()
    output_dir = input(f"    output: (default is {DEFAULT_OUTPUT_DIR}): ").strip() or DEFAULT_OUTPUT_DIR

    config = {'output_dir': output_dir}
    if default_file and Path(default_file).exists():
        config['default_input_file'] = str(Path(default_file).resolve())

    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    print("    config saved")


# 验证函数

def verify_installation():
    """验证安装"""
    print("\npackage installation")

    packages = ['pandas', 'openai', 'pypdf', 'dotenv']
    for pkg in packages:
        try:
            __import__('dotenv' if pkg == 'dotenv' else pkg)
            print(f"    + {pkg}")
        except ImportError:
            print(f"    - {pkg} not installed")


# ==========================================
# 主函数
# ==========================================
def main():

    print("BioMethodExtractor")


    # 检查
    if not check_python_version():
        print("\nerr: Python version not compatible, ")
        sys.exit(1)


    # 安装和配置
    install_dependencies()
    setup_api_key()
    setup_default_input()


    # 验证
    verify_installation()

    # 完成
    print("Finished")
    print("\nPLEASE:")
    print("  1. ensure api key is valid")
    print("  2. Put sample pdf file into    '~/tests/data'  ")
    print("  3. run 'python -m pdf.py and jsonTocsv.py'")
    print("\nfor more, please look for README.md\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInstall canceled")
        sys.exit(0)
    except Exception as e:
        print(f"\nERR: {str(e)}")
        sys.exit(1)
