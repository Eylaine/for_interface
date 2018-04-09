# coding=utf-8
# Time    : 2018-04-09
# Author  : Eylaine
# File    : confutil.py

from utils.logutil import logger
from configparser import ConfigParser


class ConfUtil(object):

    def __init__(self):
        self.config = ConfigParser()
        logger.info("读取配置文件config.ini")
        self.config.read("config/config.ini")

    def getproperty(self, section, key):
        logger.info("读取配置：%s %s" % (section, key))
        return self.config.get(section, key)

