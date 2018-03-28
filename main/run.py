# !/usr/bin/python
# _*_ coding: utf-8 _*_

# @Time    : 2018/3/16
# @Author  : zhonglin.zhang

import pytest


class GlobalConfig(object):

    URL = "https://api.github.com"
    print(locals())


if __name__ == '__main__':
    aa = GlobalConfig()
    pytest.main()
