# file: utils.py
# author: mbiokyle29

import logging


def configure_logger(logger, level):
    logger.setLevel(level)
    sh = logging.StreamHandler()
    sh.setLevel(level)
    formatter = logging.Formatter("[%(name)s][%(levelname)s]: %(message)s")
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger
