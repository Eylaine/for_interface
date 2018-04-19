# coding=utf-8
# Time    : 2018-04-09
# Author  : Eylaine
# File    : confutil.py

from utils.logutil import logger
from configparser import ConfigParser
from common import ROOTPATH


config = ConfigParser()
logger.info("读取配置文件config.ini")
config.read(ROOTPATH + "/config/config.ini")


def getproperty(section, key):
    logger.info("读取配置：%s %s" % (section, key))
    return config.get(section, key)


