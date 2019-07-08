# coding=utf-8
# Time   : 2019/6/12 17:01
# Author : zhonglin.zhang
# File   : settins.py

import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)

        return cls._instance


class Environment(Singleton):
    """
    单例模式设计，保持环境变量
    """

    ENV = "alpha"
    INI_PATH = ROOT_PATH + "/config/config.ini"
    YAML_PATH = ROOT_PATH + "/config/config.yaml"

    def set_env(self, env):
        self.ENV = env


ENV = Environment()
