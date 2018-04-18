# coding=utf-8
# Time    : 2018/3/13 22:11
# Author  : Eylaine
# File    : test_user.py

from utils.httputil import get
from utils.logutil import logger
import allure


@allure.step(u"api层")
def get_single_user():
    logger.info("开始调用api层接口===========")
    path = "/users"
    return get(path)
