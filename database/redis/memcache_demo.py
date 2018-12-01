#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-01 21:49:38
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$


# Ubuntu安装memcached: sudo apt install memcached
# 启动memcached
# memcached 
# -d                    启动一个守护进程
# -m 10                 分配给memcache使用的内存数量,单位是mb
# -u root               运行的用户
# -l 192.168.1.115      监听的服务器IP地址
# -p 12000              监听的端口号
# -c 256                最大运行的并发连接数
# -P /tmp/memcached.pid 设置保存memcache的pid地址

# 命令行连接
# telnet IP PORT

import memcache

conn = memcache.Client([("192.168.1.115:12000", 1)], debug=True)
conn.set('foo', 'bar')
ret = conn.get('foo')
print(ret)
