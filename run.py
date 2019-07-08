# !/usr/bin/python
# _*_ coding: utf-8 _*_

# @Time    : 2018/3/16
# @Author  : zhonglin.zhang

import pytest
import sys

from settins import ENV

if __name__ == '__main__':
    args = sys.argv
    env = args[1]  # 测试环境变量
    ENV.set_env(env)
    pytest_arg = args[2:]
    pytest.main(pytest_arg)
