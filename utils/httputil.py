# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : httputil.py

import requests
from utils.logutil import logger
from utils.confutil import getproperty
import json


request_session = requests.Session()
url = getproperty("github", "url")
headers = {"Authorization": getproperty("github", "token")}


def get(path, params=None, header=None):
    logger.info("发送get请求")
    return request_session.get(url=url+path, params=params, headers=header)


def post(path, data=None, header=None):
    logger.info("发送post请求")
    return request_session.post(url=url+path, data=json.dumps(data), headers=header)
