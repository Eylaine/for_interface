# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : logutil.py

import logging.config
from common import ROOTPATH


# class Singleton(object):
#     _instance = None
#
#     def __new__(cls, *args, **kw):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
#         return cls._instance
#
#
# class Log(Singleton):
#
#     @staticmethod
#     def getlogger():
#         logging.config.fileConfig(ROOTPATH + "config/logger.ini")
#         log = logging.getLogger("root")
#         return log
#

# logger = Log.getlogger()

# 指定logger输出格式
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s")
# 日志输出到文件
file_handler = logging.FileHandler(ROOTPATH + "/output/logs.log")
# 指定日志输出格式
file_handler.setFormatter(formatter)
# 获取logger实例，参数为空则返回root logger
logger = logging.getLogger()
# 添加文件日志处理器
logger.addHandler(file_handler)
# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)
