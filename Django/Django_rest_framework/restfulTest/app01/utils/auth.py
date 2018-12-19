from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView  # rest framework类
from rest_framework import exceptions  # 错误类型
from api import models

class MyAuthentication(object):
	"""
	认证用户是否登录
	类中必须有authenticate方法和authenticate_header方法
	"""

	def authenticate(self, request):
		c_token = request._request.GET.get('token', '')
		if not c_token:
			raise exceptions.AuthenticationFailed('get url not token parse')

		s_token = models.UserToken.objects.filter(token=c_token).first()
		if not s_token:
			raise exceptions.AuthenticationFailed('token vlaue is not find')

		return (s_token.user_id, s_token)  # 封装在request.user, request.auth中

	def authenticate_header(self, request):
		pass
