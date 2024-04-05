# -*- coding: utf-8 -*-

'''
app: template
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: 模板
'''


import tools

def test(*args):
    print(args)
    print(*args)

path1 = tools.ROOTPATH
checkpoint_path = tools.xpath(path1, 'test/sam_vit_h_4b8939.pth')
print(tools.xpath(path1, checkpoint_path))