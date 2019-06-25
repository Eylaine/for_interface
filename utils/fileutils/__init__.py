# coding=utf-8
# Time   : 2019/6/13 10:28
# Author : zhonglin.zhang
# File   : __init__.py

from configparser import ConfigParser
import yaml
import allure
from common import ROOTPATH

"""
基本文件类型的读写：txt， ini等
"""

config = ConfigParser()
INIPATH = "/config/config.ini"
YAMLPATH = "/config/config.yaml"


class IniFile:

    def __init__(self):
        self.file_path = ROOTPATH + INIPATH

    def get_value(self, section, key):
        config.read(self.file_path, encoding="utf-8")
        return config.get(section=section, option=key)


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
