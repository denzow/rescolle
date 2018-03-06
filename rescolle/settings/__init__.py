# coding: utf-8
import os

if os.environ.get('IS_DEVELOP'):
    from .develop import *
