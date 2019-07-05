# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : log.py

import logging
from logging import config
from settins import ROOT_PATH


def singleton(cls, *args, **kwargs):

    instance = {}

    def _instance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return _instance


@singleton
class Logger:

    def __init__(self):
        self.file_path = ROOT_PATH + "/config/logger.ini"

    def get_logger(self):
        logging.config.fileConfig(self.file_path)
        logger = logging.getLogger("root")
        return logger


log = Logger()
