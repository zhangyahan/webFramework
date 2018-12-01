#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-01 03:03:30
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$

from gzip import *
from urllib import request


url = "http://www.baidu.com/"
res = request.urlopen(url)
print(res.read().decode('utf-8'))
