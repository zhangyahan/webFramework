from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View  # CBV

# Create your views here.


def index(request):
	context = {}

	context['name'] = 'agnle'
	context['age'] = 12

	return JsonResponse(context, safe=False)



class StudentsView(View):

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



