#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-12 07:19:59
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$

"""
时间间隔
"""

import datetime

# 获取当前时间
now = datetime.datetime.now()

# 时间间隔
d7 = datetime.timedelta(weeks=1)

# 失效时间
ret = now + d7

print(ret)
