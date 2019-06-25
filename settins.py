# coding=utf-8
# Time   : 2019/6/12 17:01
# Author : zhonglin.zhang
# File   : settins.py

from utils.fileutils import IniFile

"""
单例模式设计，保持环境变量
"""


class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)

        return cls._instance


class Env(Singleton):

    def __init__(self, env='alpha'):
        # 默认alpha环境
        self.env = env

    def set_env(self, env):
        self.env = env


domain = Env()
