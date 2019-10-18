# coding=utf-8
# Time    : 2018/3/13 21:46
# Author  : Eylaine
# File    : logutil.py

import logging
import logging.config
from settins import ROOT_PATH


def log_config():
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"handlers": ["console", "file"], "level": "INFO", "propagate": False},
        # "loggers": {
        #     "console": {
        #
        #     },
        #     "file": {
        #
        #     }
        # },
        "formatters": {
            "simple": {
                "format": "[%(levelname)s] %(filename)s: %(lineno)d - %(message)s"
            },
            "complex": {
                "format": "[%(levelname)s] %(asctime)s - %(filename)s:%(lineno)d - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "level": "INFO"
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "complex",
                "level": "INFO",
                "filename": f"{ROOT_PATH}/output/log/logs.log",
                "mode": "w+",
                "encoding": "utf8"
            }
        }
    }

    logging.config.dictConfig(config)


def get_logger():
    log_config()
    return logging.getLogger("root")


logger = get_logger()


def record_log(func):

    def wrapper(*args, **kwargs):
        logger.info("")
        return func(*args, **kwargs)

    return wrapper
