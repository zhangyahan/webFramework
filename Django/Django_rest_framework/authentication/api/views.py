from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView  # rest framework类
from rest_framework import exceptions  # 错误类型
from api import models
from .utils import permission, throttle, auth
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
	permission_classes = []
	throttle_classes = [throttle.VisitThrottle, ]

	def post(self, request, *args, **kwargs):

		# 1. 去request中获取IP
		# 2. 访问记录...

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
	}}


class OrderView(APIView):

	"""
	订单相关业务(只有SVIP只有权限)
	"""

	# # 叫校验的类放入到authentication_classes属性的列表中
	# authentication_classes = [MyAuthentication, ]  # 认证
	# permission_classes = [permission.SVIPPermission,]  # 权限

	def get(self, request, *args, **kwargs):

		ret = {"code": 1000, "message": None, "data": None}

		ret['data'] = ORDER_DICT
		# print(request._request.META)
		print(request.user)  # s_token.user_id
		print(request.auth)  # s_token


		return JsonResponse(ret)


class UserInfo(APIView):

	"""
	用户信息(所有用户都能看)
	"""

	# authentication_classes = [MyAuthentication, ]

	permission_classes = [permission.OrdinaryPermission, ]  # 权限

	def get(self, request, *args, **kwargs):
		return HttpResponse('用户信息')
