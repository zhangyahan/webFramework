import json
from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.


# def get_user(request):
# 	return HttpResponse(json.dumps({'code': 200, 'data': USER_INFO}, ensure_ascii=False))


# def add_user(request):
# 	pass


# def up_data_user(request):
# 	pass


# def del_user(request):
# 	pass


# class UserView(View):

# 	def get(self, request, *args, **kwargs):
# 		return HttpResponse(json.dumps({'code': 200, 'data': USER_INFO}, ensure_ascii=False))

# 	def post(self, request,  *args, **kwargs):
# 		pass

# 	def put(self, request,  *args, **kwargs):
# 		pass

# 	def delete(self, request,  *args, **kwargs):
# 		pass	




# ######### django_rest_framework #############

USER_INFO = {
	'1': {
		'name': '张亚瀚',
		'age': 18,
		'gender': '男',
	},
	'2': {
		'name': '王花花',
		'age': 18,
		'gender': '女',
	},
	'3': {
		'name': '李狗蛋',
		'age': 18,
		'gender': '男',
	},

}


from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions

class MyAuthentication(object):
	def authenticate(self, request):
		#获取用户名和密码
		token = request._request.GET.get('token')
		uid = request._request.GET.get('uid')
		name = request._request.GET.get('name')

		user_dict = USER_INFO.get(str(uid))
		user = user_dict.get('name')
		if name == user and token:
			return (user, None)  # 返回的对象存放在request.user中
		else:
			raise exceptions.AuthenticationFailed('验证未通过')
		

	def authenticate_header(self, val):
		pass


class UserView(APIView):
	
	authentication_classes = [MyAuthentication,]

	def get(self, request, *args, **kwargs):
		print(request)
		print(request.user)
		return HttpResponse(json.dumps({'code': 200, 'data': USER_INFO}, ensure_ascii=False))

	def post(self, request,  *args, **kwargs):
		pass

	def put(self, request,  *args, **kwargs):
		pass

	def delete(self, request,  *args, **kwargs):
		pass	