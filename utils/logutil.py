# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : logutil.py

import logging.config


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class Log(Singleton):
    def __init__(self):
        logging.config.fileConfig("config/logger.ini")
        self.logger = logging.getLogger("root")

    def debug(self, msg):
        self.logger.debug(msg=msg)

    def info(self, msg):
        self.logger.info(msg=msg)

    def error(self, msg):
        self.logger.error(msg=msg)

    def warning(self, msg):
        self.logger.warning(msg=msg)


logger = Log()
