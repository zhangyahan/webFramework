#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 22:16:19
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$


# 基类
class Base(object):
	XX = 123


# 发布
class Pro(Base):
	DEBUG = False


# 生产
class Dev(Base):
	DEBUG = True
