from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin

"""
	自定义中间件
"""

URL = ['/oo/', '/xx/']

class OneMiddleWare(MiddlewareMixin):

	def process_request(self, request):
		print('这是我的第一个中间件')
		# request_url = request.path_info
		# # 如果返回的是None则继续执行
		# if request_url in URL:
		# 	return
		# else:
		# 	# 如果返回的是HttpResponse对象,则返回给用户
		# 	return HttpResponse('不OK')

	def process_response(self, request, response):
		print('这是我的第一个中间件的response方法')
		return response

class TwoMiddleWare(MiddlewareMixin):

	def process_request(self, request):
		print('这是我的第二个中间件')

	def process_response(self, request, response):
		print('这是我的第二个中间件的response方法')
		return response