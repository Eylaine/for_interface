# coding=utf-8
# Time    : 2018/3/13 22:11
# Author  : Eylaine
# File    : test_user.py

from api.user import User
import json
from utils.logutil import LogUtil

user = User()
logger = LogUtil()


def test_get_single_user():
    res = user.get_single_user()
    code = res.status_code
    data = json.loads(res.content)
    # print(json.loads(res.content))
    logger.info(code)