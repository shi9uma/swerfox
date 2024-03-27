# -*- coding: utf-8 -*-

'''
app: tools
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: utils tools 入口
'''

# packages imports
import sys

sys.path.append('.')
# custom util imports
import utils.path_handler as path
import utils.decorator as decorator
import utils.template as template
import utils.telescope as telescope


# GLOBAL
ROOTPATH = path.get_root_path()
CONFIGPATH = '{}/{}'.format(ROOTPATH, 'resources/config')


# _path
@decorator.decorator_logging
def dirname(path):
    '''
    wrapper for os.path.dirname(path)
    '''
    return path.dirname(path)


@decorator.decorator_logging
def gen_template(app_name: str = 'template', config_name: str = 'main'):
    '''
    生成模板\n
    app = tools.gen_template('app', 'main')\n
    只填文件名，自动补全：main -> resources/config/main.json\n
    不填默认 main
    '''
    if config_name == '':
        config_name = 'main'
    return template.template(app_name, '{}/{}.json'.format(CONFIGPATH, config_name))

# telescope
@decorator.decorator_logging
def get_dict_dict(dict_obj: dict) -> dict:
    '''
    以字典形式展示字典中各个值
    '''
    return telescope.get_dict_dict(dict_obj)

@decorator.decorator_logging
def get_dict_list(dict_obj: dict) -> list:
    '''
    以列表形式展示字典中各个值    
    '''
    return telescope.get_dict_list(dict_obj)

@decorator.decorator_logging
def get_class_attr(class_obj: object) -> dict:
    '''
    以字典形式展示类中各个属性
    '''
    return telescope.get_class_attr(class_obj)