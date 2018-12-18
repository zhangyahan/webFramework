from django.shortcuts import render, HttpResponse

# Create your views here.

def app01_index(request):
	print('这是app01中的第一个视图函数')
	return HttpResponse('哈哈哈哈哈哈')

