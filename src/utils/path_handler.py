# -*- coding: utf-8 -*-

'''
app: utils.decorator
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: 目录操作函数
'''

# imports
import os

# functions
def dirname(path):
    '''
    wrapper for os.path.dirname(path)
    '''
    return os.path.dirname(path)

def get_root_path():
    '''
    获取整个项目的根目录
    '''
    return dirname(dirname(dirname(os.path.realpath(__file__))))