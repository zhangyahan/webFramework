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
		           jsonify,
		           Markup,
		           flash,
		           get_flashed_messages)
import functools

app = Flask(__name__)
# 导入配置文件
app.config.from_object('settings.Dev')

STUDENT_DICT = {
	1:{'name': '王花花', 'age': 21, 'gender': '女'},
	2:{'name': '李狗蛋', 'age': 18, 'gender': '男'},
	3:{'name': '王铁花', 'age': 38, 'gender': '女'},
}


@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == "GET":
		return render_template('login.html')
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	if username == 'zyh' and password == '123456':
		session['username'] = username
		return redirect(url_for('index'))
	return render_template('login.html', error_message='用户名或密码错误')

# @app.before_request
# def xxxxxx():
# 	if request.path == '/login':
# 		return None
# 	if not session.get('username', ''):
# 		return '滚'


@app.route('/')
@app.route('/index', endpoint='index')
def index():
	stud = STUDENT_DICT
	return render_template('index.html', stud=stud)


@app.route('/delinfo/<int:nid>')
def delinfo(nid):
	if nid in STUDENT_DICT:
		del STUDENT_DICT[nid]

	return redirect(url_for('index'))


@app.route('/catinfo/<int:nid>')
def catinfo(nid):
	info = STUDENT_DICT[nid]
	return render_template('info.html', info=info)

@app.template_global()
def func(num):
	return num + 1

@app.template_filter()
def func_params(a, b, c):
	return a + b + c

@app.route('/tpl')
def tpl():
	context = {
		'users': ['王花花', '李狗蛋', '赵铁柱'],
		'txt': Markup('<input type="text">'),
	}
	print()
	return render_template('tpl.html', **context)


@app.route('/page1')
def page1():
	# session['uuu'] = 123
	flash('临时数据存储')
	return '1'


@app.route('/page2')
def page2():
	# print(session['uuu'])
	print(get_flashed_messages())
	return '2'

if __name__ == '__main__':
	app.run()
