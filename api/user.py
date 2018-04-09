# coding=utf-8
# Time    : 2018/3/13 22:11
# Author  : Eylaine
# File    : test_user.py

from utils.httputil import HttpUtil
from utils.logutil import Log

logger = Log()
httputil = HttpUtil()


def get_single_user():
    logger.info("开始调用api层接口")
    path = "/users"
    return httputil.get(path)
