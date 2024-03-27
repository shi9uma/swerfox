# -*- coding: utf-8 -*-

'''
app: utils.decorator
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: 各种装饰器
'''

import sys
import logging

def decorator_logging(func):
    '''
    日志装饰器
    '''
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except Exception as e:
            logging.error(e)
            sys.exit(1)
    return wrapper
