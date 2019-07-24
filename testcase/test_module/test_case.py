# coding=utf-8
# Time    : 2018/3/13 22:11
# Author  : Eylaine
# File    : test_case.py

import allure


@allure.feature(u"测试用例执行")
class TestUser:

    def test_pass(self):
        assert True

    def test_fail(self):
        assert False
