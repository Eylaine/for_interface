# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : http.py

import requests
from utils import log
import json


def get(path, params=None, header=None):
    log.info("发送get请求")
    return requests.get(url=path, params=params, headers=header)


def post(path, data=None, header=None):
    log.info("发送post请求")
    return requests.post(url=path, data=json.dumps(data), headers=header)


def put(path, data=None, **kwargs):
    return requests.put(url=path, data=json.dumps(data), **kwargs)


def delete(path, data=None, **kwargs):
    return requests.delete(url=path, data=json.dumps(data), **kwargs)
