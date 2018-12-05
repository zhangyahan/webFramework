from flask import Flask, views
import functools


app = Flask(__name__)


def wrapper(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		return func(*args, **kwargs)

	return inner

class UserView(views.MethodView):
	methods = ['GET']  # 指定允许的方法
	decorators = [wrapper,]  # 指定装饰器
	def get(self, *args, **kwargs):
		return "GET"

	def post(self, *args, **kwargs):
		return "POST"


app.add_url_rule(rule='/user',
				 endpoint=None, 
				 view_func=UserView.as_view('uuuu'))


if __name__ == '__main__':
	app.run(debug=True)
		