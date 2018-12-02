#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 22:10:49
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$

from flask import (Flask,
				   render_template,
		           request,
		           redirect,
		           session,
		           url_for,
		           jsonify)

app = Flask(__name__)
# 导入配置文件
app.config.from_object('settings.Dev')

# 反向解析
@app.route('/index/<int:nid>', 
		   methods=['POST', 'GET'],
		   endpoint='name1')
# endpoint就是Django中的name,不写默认是函数名
# url_for反向生成url
def index(nid):
	print('url>>>>>', url_for('name1', nid=nid))
	print(nid)
	print(dir(request))
	return "index"
	return render_template()
	return redirect()
	dic = {'k1': "v1"}
	return jsonify(dic)


if __name__ == '__main__':
	app.run()
