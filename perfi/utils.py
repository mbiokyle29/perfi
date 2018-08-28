# file: utils.py
# author: mbiokyle29

import logging
from enum import Enum


class Every(Enum):

    DAY = "daily"
    MONTH = "monthly"
    YEAR = "yearly"

    @classmethod
    def convert_amount(cls, from_e, to_e, amount):
        """ Convert an amount over one time frame to another """

        if from_e is to_e:
            return amount
        elif from_e is cls.DAY:
            multiplyer = 30.416 if to_e is cls.MONTH else 365
        else:
            multiplyer = (1 / 354) if to_e is cls.DAY else (1 / 12)

        return multiplyer * amount


def configure_logger(logger, level):
    logger.setLevel(level)
    sh = logging.StreamHandler()
    sh.setLevel(level)
    formatter = logging.Formatter("[%(name)s][%(levelname)s]: %(message)s")
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


def format_percent(percent):
    return f"{percent * 100:.3f}%"


def format_dollar_amount(dollar_amount):
    return f"-${abs(dollar_amount):.2f}" if dollar_amount < 0 else f"${dollar_amount:.2f}"
