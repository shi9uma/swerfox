# -*- coding: utf-8 -*-

'''
app: template
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: 模板
'''

# packages imports


# custom util imports


# functions

import utils.path_handler as path
class template:
    def __init__(self, app_name: str = 'template', config_path: str = 'resources/config/template.json'):
        self.root_path = path.get_root_path()
        self.app_name = app_name
        self.config_path = config_path
