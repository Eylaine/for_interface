# -*- coding: utf-8 -*-
# @Time    : 2019-07-24 20:11
# @Author  : zhonglin.zhang
# @File    : contest.py

import pytest

from api import login


def get_data_list():
    pass


def get_user_list():
    pass


@pytest.fixture(params=get_user_list(), scope="module")
def pre_login(request):
    yield login(**(request.param))


@pytest.fixture(params=get_data_list(), scope="session")
def data_provider(request):
    yield request.param
