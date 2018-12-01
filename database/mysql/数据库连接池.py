#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-01 20:54:37
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$


# 不用连接池的mysql连接方法
# import pymysql
# db = pymysql.connect(host='localhost',
# 					   port=3306,
# 					   user='zyh1',
# 					   password='zyh1997',
# 					   db='demo',
# 					   charset='utf8')

# cur = db.cursor()
# sql = 'select * from 01_demo'
# cur.execute(sql)
# res = cur.fetchall()
# print(res)
# cur.close()
# db.close()



# 使用连接池
import pymysql
from DBUtils.PooledDB import PooledDB
from threading import Thread
from multiprocessing import Process
import time
import sys
pool = PooledDB(pymysql, maxconnections=3,
				blocking=False,  # 5为连接池里的最小连接数
				host='localhost',
				port=3306,
				user='zyh1',
				password='zyh1997',
				db='demo',
				charset='utf8')
def select_data():
	try:
		db = pool.connection()  # 以后每次需要数据库连接就用connection()函数获取连接
	except Exception as e:
		print('连接数超出上限', e)
		return
	cur = db.cursor()
	sql = 'select * from 01_demo'
	time.sleep(1)
	cur.execute(sql)
	res = cur.fetchall()
	print(res)
	cur.close()
	db.close()


t_list = []
for i in range(10):
	t = Thread(target=select_data)
	t_list.append(t)

for i in t_list:
	i.start()

for i in t_list:
	i.join()

print('主程序执行完毕')



# PooledDB的参数
# mincached: 最少的空闲连接数,如果空闲连接数小于这个数,pool会创建一个新的连接
# maxcached: 最大的空闲连接数,如果空闲连接数大于这个数,pool会关闭空闲连接
# maxconnections: 最大的连接数
# blocking: 当连接数达到最大连接数时,如果设置为True则阻塞等待,为False报错
# 