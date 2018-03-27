# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : logutil.py

import logging.config


logging.config.fileConfig("config/logger.ini")
logger = logging.getLogger("root")


def debug(msg):
    logger.debug(msg=msg)


def info(msg):
    logger.info(msg=msg)


def error(msg):
    logger.error(msg=msg)


def warning(msg):
    logger.warning(msg=msg)
