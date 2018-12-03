from flask import Flask



app = Flask(__name__)

@app.route('/')
@app.route('/index')
def indnex():
	return 'index'


class MiddleWare(object):
	"""docstring for MiddleWare"""
	def __init__(self, old):
		self.old = old

	def __call__(self, *args, **kwargs):
		print('前')
		ret = self.old(*args, **kwargs)
		print('后')
		return ret

if __name__ == '__main__':
	app.wsgi_app = MiddleWare(app.wsgi_app)
	app.run(debug=True)