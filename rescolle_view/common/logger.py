# coding: utf-8

import logging

logger = logging.getLogger('rescolle')


def info(msg):
    logger.info(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def debug(msg):
    logger.debug(msg)

