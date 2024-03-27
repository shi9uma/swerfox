# -*- coding: utf-8 -*-

'''
app: utils.telescope
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: 各种查看函数
'''

def get_dict_dict(dict_obj: dict) -> dict:
    '''
    以字典形式展示字典中各个值
    '''
    dict_obj_container = dict()
    for key, value in dict_obj.items():
        dict_obj_container[key] = value
    return dict_obj_container

def get_dict_list(dict_obj: dict) -> list:
    '''
    以列表形式展示字典中各个值    
    '''
    dict_obj_container = list()
    for key, value in dict_obj.items():
        dict_obj_container.append([key, value])
    return dict_obj_container

def get_class_attr(class_obj: object) -> dict:
    '''
    以字典形式展示类中各个属性
    '''
    class_obj_attrs = [attr for attr in dir(class_obj) if not attr.startswith('__')]
    class_obj_container = dict()
    for attr in class_obj_attrs:
        class_obj_container[attr] = getattr(class_obj, attr)
    return class_obj_container