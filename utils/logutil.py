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

    @staticmethod
    def getlogger():
        logging.config.fileConfig("config/logger.ini")
        log = logging.getLogger("root")
        return log


logger = Log.getlogger()
