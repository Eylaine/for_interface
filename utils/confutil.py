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
        try:
            self.config.read("config/config.ini")
        except IOError:
            logger.error(u"未找到配置文件")

    def getproperty(self, section, key):
        logger.info("读取配置：%s %s" % (section, key))
        value = self.config.get(section, key)
        if value == "":
            logger.error(u"未读取到配置信息：%s %s" % (section, key))
            raise Exception
        return value

