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
import utils.path_handler as path_handler
import utils.decorator as decorator
import utils.template as template
import utils.telescope as telescope

# GLOBAL
ROOTPATH = path_handler.get_root_path()
CONFIGPATH = '{}/{}'.format(ROOTPATH, 'resources/config')

# homo
某科学的 = decorator.某科学的

# _path
@decorator.观测之石
def dirname(path):
    '''
    wrapper for os.path.dirname(path)
    '''
    return path_handler.dirname(path)

@decorator.观测之石
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

@decorator.观测之石
def xpath(*args):
    '''
    去掉双斜杠, 多个传入则自动拼接
    '''
    return path_handler.xpath(*args)

# telescope
@decorator.观测之石
def 色色(text: str = '', color: int = 1) -> str:
    '''
    返回对应的控制台 ANSI 颜色
    '''
    return telescope.色色(text, color)

@decorator.观测之石
def get_dict_dict(dict_obj: dict) -> dict:
    '''
    以字典形式展示字典中各个值
    '''
    return telescope.get_dict_dict(dict_obj)

@decorator.观测之石
def get_dict_list(dict_obj: dict) -> list:
    '''
    以列表形式展示字典中各个值    
    '''
    return telescope.get_dict_list(dict_obj)

@decorator.观测之石
def get_class_attr(class_obj: object) -> dict:
    '''
    以字典形式展示类中各个属性
    '''
    return telescope.get_class_attr(class_obj)

@decorator.观测之石
def 看一下有没有非法元素(_组合类型, _合法元素类型):
    '''
    查看传入的组合有没有指定以外的非法元素
    '''
    return telescope.看一下有没有非法元素(_组合类型, _合法元素类型)