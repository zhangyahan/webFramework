#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 19:37:18
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$

import pika

# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()  # 创建频道

channel.queue_declare(queue='hello')  # 创建管道
while True:
	msg = input('>>>')
	channel.basic_publish(exchange='',
						  routing_key='hello',
						  body=msg)  # 发送消息

	print('发送成功')

connection.close()  # 关闭连接