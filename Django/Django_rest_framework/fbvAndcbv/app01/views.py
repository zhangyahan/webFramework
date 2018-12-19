from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator

# Create your views here.


@csrf_exempt  # 该函数不使用csrf验证
def Student(request):
	return HttpResponse('Student')



class MyBaseView(object):
	@method_decorator(csrf_exempt)  # 不使用csrf验证
	def dispatch(self, request, *args, **kwargs):
		print('before')
		ret = super(MyBaseView, self).dispatch(request, *args, **kwargs)
		print('after')
		return ret


class StudentsView(MyBaseView, View):

	# def dispatch(self, request, *args, **kwargs):
	# 	# 反射找到对应的函数
	# 	func = getattr(self, request.method.lower())
	# 	# 执行函数
	# 	ret = func(request, *args, **kwargs)
	# 	# 返回执行结果
	# 	return ret

	# def dispatch(self, request, *args, **kwargs):
	# 	print('before')
	# 	ret = super(StudentsView, self).dispatch(request, *args, **kwargs)
	# 	print('after')
	# 	reutrn ret

	def get(self, request, *args, **kwargs):
		return HttpResponse('GET')

	def post(self, request, *args, **kwargs):
		return HttpResponse('POST')

	def put(self, request, *args, **kwargs):
		return HttpResponse('POST')

	def delete(self, request, *args, **kwargs):
		return HttpResponse('POST')



class TeachersView(MyBaseView, View):

	# def dispatch(self, request, *args, **kwargs):
	# 	# 反射找到对应的函数
	# 	func = getattr(self, request.method.lower())
	# 	# 执行函数
	# 	ret = func(request, *args, **kwargs)
	# 	# 返回执行结果
	# 	return ret

	# def dispatch(self, request, *args, **kwargs):
	# 	print('before')
	# 	ret = super(TeachersView, self).dispatch(request, *args, **kwargs)
	# 	print('after')
	# 	reutrn ret

	def get(self, request, *args, **kwargs):
		return HttpResponse('GET')

	def post(self, request, *args, **kwargs):
		return HttpResponse('POST')

	def put(self, request, *args, **kwargs):
		return HttpResponse('POST')

	def delete(self, request, *args, **kwargs):
		return HttpResponse('POST')
