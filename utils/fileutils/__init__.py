# coding=utf-8
# Time   : 2019/6/13 10:28
# Author : zhonglin.zhang
# File   : __init__.py

from configparser import ConfigParser
from configparser import NoOptionError, NoSectionError
import yaml
import allure
from common import ROOTPATH
from utils.logutil import logger

"""
基本文件类型的读写：txt， ini等
"""

config = ConfigParser()
INIPATH = "/config/config.ini"
YAMLPATH = "/config/config.yaml"


class IniFile:

    def __init__(self):
        self.file_path = ROOTPATH + INIPATH

    def get_value(self, section, option):
        config.read(self.file_path, encoding="utf-8")
        try:
            value = config.get(section=section, option=option)
            if value is "":
                logger.error(u"未获取到配置，请检查配置项")
            return value
        except NoSectionError:
            logger.error(u"请检查section是否正确：" + section)
        except NoOptionError:
            logger.error(u"请检查option是否正确：" + option)


class YamlFile:

    @staticmethod
    @allure.step("获取域名domain，env={0}，key={1}")
    def get_domain(env, key):
        default_path = ROOTPATH + YAMLPATH
        with open(default_path, mode='r', encoding='utf-8') as yl:
            data = yaml.load(yl, Loader=yaml.Loader)

        return data[env][key]

    @staticmethod
    def read(file_path):
        with open(file_path, mode='r+', encoding='utf-8') as yl:
            return yaml.load(yl, Loader=yaml.Loader)
