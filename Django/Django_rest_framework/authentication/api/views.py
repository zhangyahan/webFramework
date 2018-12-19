from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView  # rest framework类
from rest_framework import exceptions  # 错误类型
from api import models
# Create your views here.


def md5(user):
	"""md5加密"""
	import hashlib
	import time

	ctime = str(time.time())  # 获取当前时间戳, 并转换成字符串
	m = hashlib.md5(bytes(user, encoding='utf-8'))  # 实例对象, 并加盐
	m.update(bytes(ctime, encoding='utf-8'))  # 将数据转换成密文

	return m.hexdigest()


class AuthView(APIView):
	"""
	用户登录认证, 并保存token
	"""

	authentication_classes = []

	def post(self, request, *args, **kwargs):
		self.dispatch
		ret = {"code": 1000, "message": None}

		try:
			username = request._request.POST.get('username')
			password = request._request.POST.get('password')
			user_obj = models.UserInfo.objects.filter(username=username, password=password).first()

			if not user_obj:
				raise ValueError('用户名或密码错误')

			# 为登录用户创建token
			token = md5(username)
			# 存在则更新, 不存在则创建
			models.UserToken.objects.update_or_create(user=user_obj, defaults={'token': token})
			ret['token'] = token

		except ValueError as e:
			ret['code'] = 1001
			ret['message'] = str(e)

		except Exception as e:
			ret['code'] = 1002
			ret['message'] = '请求异常'

		return JsonResponse(ret)



ORDER_DICT = {
	1:{
		"name": "媳妇",
		"age": 18,
		"gender": "男",
		"content": "xxx",
	},
	2:{
		"name": "小狗",
		"age": 1,
		"gender": "雄",
		"content": "xxx",
	}
}


class OrderView(APIView):
	# # 叫校验的类放入到authentication_classes属性的列表中
	# authentication_classes = [MyAuthentication, ]

	def get(self, request, *args, **kwargs):
		ret = {"code": 1000, "message": None, "data": None}

		ret['data'] = ORDER_DICT
		print(request.user)  # s_token.user_id
		print(request.auth)  # s_token

		# try:
		# 	c_token = request._request.GET.get('token', '')

		# 	if c_token:
		# 		s_token = models.UserToken.objects.filter(token=c_token)
		# 		if c_token == s_token:
		# 			ret['data'] = ORDER_DICT
		# 		else:
		# 			ret['message'] = "token vlaue is not find"
		# 	else:
		# 		ret['message'] = "get url not token"

		# except Exception as e:
		# 	ret['code'] = 1002
		# 	ret['message'] = '请求异常'

		return JsonResponse(ret)


class UserInfo(APIView):

	# authentication_classes = [MyAuthentication, ]

	def get(self, request, *args, **kwargs):
		return HttpResponse('用户信息')
