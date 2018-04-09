# coding=utf-8
# Time    : 2018/3/13 22:11
# Author  : Eylaine
# File    : test_user.py

from api.user import *


class TestUser(object):

    def test_get_single_user(self):
        res = get_single_user()
        code = res.status_code

        if code != 200:
            # self.fail("状态码不正确")
            pass
        data = res.json()
