#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 21:47:58
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$


import importlib

path = 'sys.path'

p, c = path.split('.')  # 进行字符串分割
m = importlib.import_module(p)  # 获模块名
cls = getattr(m, c)  # 获取对象
print(cls)
