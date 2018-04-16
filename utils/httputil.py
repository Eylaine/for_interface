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

    def get(self, path, **kwargs):
        logger.info("发送不带参数的get请求，无headers")
        return self.request_session.get(url=self.url + path, **kwargs)

    def get(self, path, params=None, **kwargs):
        logger.info("发送带参数get请求，无headers")
        if params is None:
            return self.request_session.get(path)
        return self.request_session.get(url=self.url + path, parmas=params, **kwargs)

    def post(self, path, **kwargs):
        logger.info("发送无参post请求")
        return self.request_session.post(url=self.url + path, headers=self.headers, **kwargs)

    def post(self, path, data=None, **kwargs):
        logger.info("发送post请求")
        if data is None:
            return self.request_session.post(path)
        return self.request_session.post(url=self.url + path, data=json.dumps(data), **kwargs)


httputil = HttpUtil()
