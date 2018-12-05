from flask import Flask

app = Flask(__name__)


# 步骤一: 定制类
from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
	"""
	自定义URl匹配正则表达式
	"""
	def __init__(self, map, regex):
		super(RegexConverter, self).__init__(map)
		self.regex = regex

	def to_python(self, value):
		"""
		转换属性
		"""
		return int(value)

	def to_url(self, value):
		"""
		反向生成url
		"""
		url = super(RegexConverter, self).to_url(value)
		return url


# 步骤二: 添加到转换器
app.url_map.converters['reg'] = RegexConverter

# 使用
@app.route('/index/<reg("\d+"):nid>')
def index(nid):
	return 'index'


if __name__ == '__main__':
	app.run(debug=True)