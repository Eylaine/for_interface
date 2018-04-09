# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : httputil.py

import requests
from utils.logutil import Singleton, Log
from utils.confutil import config


class HttpUtil(Singleton):
    logger = Log()

    def __init__(self):
        self.request_session = requests.Session()
        self.url = config.getproperty("GITHUB", "url")
        self.headers = {"Authorization": config.getproperty("GITHUB", "token")}

    def get(self, path, **kwargs):
        self.logger.debug("发送get请求")
        return self.request_session.get(url=self.url + path, headers=self.headers, **kwargs)

    def post(self, path, **kwargs):
        self.logger.info("发送post请求")
        return self.request_session.post(url=self.url + path, headers=self.headers, **kwargs)
