#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 21:04:43
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
	print('>>>>>>', body)

channel.basic_consume(callback, queue='hello', no_ack=True)

print('等待消息, 退出按Ctrl + C')

channel.start_consuming()
