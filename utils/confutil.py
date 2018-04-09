# coding=utf-8
# Time    : 2018-04-09
# Author  : Eylaine
# File    : confutil.py

from utils.logutil import Singleton, Log
from configparser import ConfigParser


class ConfUtil(Singleton):
    logger = Log()

    def __init__(self):
        self.config = ConfigParser()
        self.logger.info("读取配置文件config.ini")
        self.config.read("config/config.ini")

    def getproperty(self, section, key):
        self.logger.info("读取配置：%s %s" % (section, key))
        return self.config.get(section, key)


config = ConfUtil()

