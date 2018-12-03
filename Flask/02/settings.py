#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 22:16:19
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$

import random
import string
from datetime import timedelta


# 基类
class Base(object):
	code = ''.join(random.sample(string.ascii_letters + string.digits, 21))
	SECRET_KEY = code
	SESSION_COOKIE_NAME = 'session'
	PERMANENT_SESSION_LIFERIME = timedelta(hours=1)



# 发布
class Pro(Base):
	DEBUG = False


# 生产
class Dev(Base):
	DEBUG = True
