#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-01 22:54:08
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$

# 普通连接
# import redis

# r = redis.Redis(host='127.0.0.1', port=6379)
# r.set('foo', 'bar')
# print(r.get('foo'))


# 连接池连接
# import redis

# # 创建连接池
# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

# # 每个连接都到连接池中取
# r = redis.Redis(connection_pool=pool)
# r.set('foo', 'bar')
# print(r.get('foo'))


# 事务
# import redis

# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

# r = redis.Redis(connection_pool=pool)

# # 设置事务
# pipe = r.pipeline(transaction=True)
# # 开启事务
# pipe.multi()
# pipe.set('name', 'alex')
# pipe.set('role', 'sb')
# pipe.execute()
# 
# 实现计数器
# import redis

# conn = redis.Redis(host='127.0.0.1', port=6379)

# conn.set('count', 1000)

# with conn.pipeline() as pipe:

# 	# 先监视自己的值没有被修改
# 	conn.watch('count')

# 	# 事务开启
# 	pipe.multi()
# 	old_count = conn.get('count')
# 	count = int(old_count)

# 	if count > 0: # 代表有库存
# 		pipe.set('count', count - 1)

# 	# 执行,把所有命令一次推送出去
# 	pipe.execute()



# 发布和订阅
import redis

class RedisHelper(object):

	def __init__(self):
		self.__conn = redis.Redis(host='127.0.0.1')
		self.chan_sub = 'fm104.5'
		self.chan_pub = 'fm104.5'

	def public(self, msg):
		self.__conn.publish(self.chan_pub, msg)
		return True

	def subscribe(self):
		pub = self.__conn.pubsub()
		pub.subscribe(self.chan_sub)
		pub.parse_response()
		return pub


# 订阅者
obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
	msg = redis_sub.parse_response()
	print(msg)


# 发布者
obj = RedisHelper()
obj.public('hello')


