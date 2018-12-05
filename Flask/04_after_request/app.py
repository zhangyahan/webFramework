from flask import Flask


app = Flask(__name__)


@app.before_first_request
def x1():
	print('123123')


@app.after_request
# 必须要有个参数,必须要有个返回值
def x2(respon):
	print('after:x1')
	return respon

@app.after_request
# 必须要有个参数,必须要有个返回值
def xx2(respon):
	print('after:xx2')
	return respon


@app.route('/index')
def index():
	print('index')
	return "Index"

if __name__ == '__main__':
	app.run(debug=True)
