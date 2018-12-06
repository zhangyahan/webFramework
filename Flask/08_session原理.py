from flask import Flask

# 实例化flask对象
app = Flask(__name__)


# 设置路由
@app.route('/index')
def index():
	return 'index'

if __name__ == '__main__':
	# 启动socket服务器
	app.run(debug=True)

	# 当请求进来,执行__call__方法
	