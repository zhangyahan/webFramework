from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import BaseVersioning, QueryParameterVersioning, URLPathVersioning
from django.urls import reverse

# Create your views here.

class UserView(APIView):

	# versioning_class = QueryParameterVersioning  # 使用内置的获取版本的类, 需要在配置中设置
	# versioning_class = URLPathVersioning  # 使用URL路径方式获取版本类, 需在路由中配置

	def get(self, request, *args, **kwargs):
		version = request.version  # 使用URL获取版本号, 仍然实在request.version中
		print(version)
		print(request.versioning_scheme)  # 使用的版本类的对象, 对象中有一个reverse方法用于反向生成对象(rest_framework)
		print(request.versioning_scheme.reverse(viewname="user", request=request))  # 参数为别名和版本号

		print(reverse(viewname="user", kwargs=({"version":version})))  # 基于Django内置

		return HttpResponse('xxx')



class DjangoView(APIView):

	def get(self, request, *args, **kwargs):
		return HttpResponse('POST和Body')
