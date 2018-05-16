# coding=utf-8
# Time    : 2018-04-09
# Author  : Eylaine
# File    : confutil.py

from utils.logutil import logger
from configparser import ConfigParser
from configparser import NoSectionError, NoOptionError
from common import ROOTPATH


config = ConfigParser()
logger.info(u"读取配置文件config.ini")
config.read(ROOTPATH + "/config/config.ini")


def getproperty(section, option):
    logger.info(u"读取配置：%s %s" % (section, option))

    try:
        value = config.get(section, option)
        if value == "":
            logger.error(u"未获取到配置，请检查配置项")
        return value
    except NoSectionError:
        logger.error(u"请检查section是否正确：" + section)
    except NoOptionError:
        logger.error(u"请检查option是否正确：" + option)

