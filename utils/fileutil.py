# coding=utf-8
# Time   : 2019/7/5 15:45
# Author : zhonglin.zhang
# File   : fileutil.py

import allure
from configparser import ConfigParser, NoSectionError, NoOptionError
import yaml
from jsonpath import jsonpath

from settins import ENV
from .logutil import logger


@allure.step(u"获取ini文件配置")
def get_ini_value(section, option, file_path=None):
    """
    获取ini配置文件内容
    :param section: ini文件的section
    :param option: option
    :param file_path: 可以不传，默认使用config.ini文件
    :return:
    """
    config = ConfigParser()

    if file_path is None:
        config.read(ENV.INI_PATH, encoding='utf-8')
    else:
        config.read(file_path, encoding='utf-8')

    try:
        value = config.get(section, option)
        if value == "":
            logger.error(u"未获取到配置，请检查配置项")
        return value
    except NoSectionError:
        logger.error(u"请检查section是否正确：" + section)
    except NoOptionError:
        logger.error(u"请检查option是否正确：" + option)


@allure.step(u"获取yaml文件配置")
def get_yaml_value(key_path, file_path=None):
    """
    根据json path获取yaml文件内容，json path不需要带环境的路径[alpha、prod]
    :param key_path: json path
    :param file_path: yaml文件路径，不传时使用默认config配置
    :return: json path返回的是个数组，我们一般默认是精确定位，所以取索引：0
    """
    if file_path is None:
        with open(ENV.YAML_PATH, mode='r+', encoding='utf-8') as yml:
            """环境区分，所以json path不用带环境的路径"""
            data = yaml.load(yml, Loader=yaml.Loader)[ENV.ENV]
        return jsonpath(data, key_path)[0]
    else:
        with open(file_path, mode='r+', encoding='utf-8') as yml:
            data = yaml.load(yml, Loader=yaml.Loader)
            return jsonpath(data, key_path)[0]
