# coding=utf-8
# Time    : 2018/3/13 22:11
# Author  : Eylaine
# File    : test_user.py

from utils.httputil import *


class User(object):

    def __init__(self):
        pass

    def get_single_user(self):
        path = "/users"
        return get(path)
