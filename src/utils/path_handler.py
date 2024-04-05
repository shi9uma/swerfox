# -*- coding: utf-8 -*-

'''
app: utils.decorator
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: 目录操作函数
'''

# imports
import os

# self
import utils.telescope as telescope

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

def xpath(*args):
    '''
    去掉双斜杠, 多个传入则自动拼接
    '''
    def _去掉双斜杠(path: str):
        return path.replace('\\', '/').replace('\\\\', '/')
    
    if len(args) > 1:
        base_path = args[0]
        telescope.看一下有没有非法元素(args, str)
        for _path in args[1:]:
            base_path = os.path.join(base_path, str(_path))
        return _去掉双斜杠(base_path)
    return _去掉双斜杠(args[0])