# file: main.py
# author: mbiokyle29
import logging
import os
import sys

from click import argument, command, option, Path

from perfi.utils import configure_logger

root_logger = logging.getLogger("perfi")


@command()
@option("-v", "--verbose", default=False, is_flag=True, help="Enable verbose logging.")
@option("-d", "--debug", default=False, is_flag=True, help="Enable debug logging.")
def cli(verbose, debug):
    configure_logger(root_logger, logging.INFO)
    root_logger.info("Starting perfi!")
