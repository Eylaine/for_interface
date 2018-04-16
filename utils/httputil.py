# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : httputil.py

import requests
from utils.logutil import logger
from utils.confutil import ConfUtil
import json


class HttpUtil(object):

    config = ConfUtil()

    def __init__(self):
        self.request_session = requests.Session()
        self.url = self.config.getproperty("github", "url")
        self.headers = {"Authorization": self.config.getproperty("github", "token")}

    def get(self, path, params=None, **kwargs):
        logger.info("发送get请求")
        return self.request_session.get(url=self.url + path, params=params, **kwargs)

    def post(self, path, data=None, **kwargs):
        logger.info("发送post请求")
        return self.request_session.post(url=self.url + path, data=json.dumps(data), **kwargs)


httputil = HttpUtil()
