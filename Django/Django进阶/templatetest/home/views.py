from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
	return render(request, 'home.html')


# function base view
def login(request):
	if request.method == "GET":
		return render(request, 'login.html')
	else:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		return HttpResponse(username+password)


from django.views import View
# class base view
class Login(View):

	# get method
	def get(self, request):
		return render(request, 'login.html')

	# post method
	def post(self, request):
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		return HttpResponse(username+password)


def upload(request):
	if request.method == 'POST':
		# 获取文件的名字
		filename = request.FILES.get('file1').name

		# 在当前打开文件开始写
		with open(filename, 'wb') as f:
			# 使用文件对象.chunrs()获取文件内容
			for i in request.FILES['file1'].chunks():
				f.write(i)


		return HttpResponse('OK')


def json_data(request):
	# context = {'name': '小黑', 'age': 12}
	context = [1, 2, 3]
	# import json
	from django.http import JsonResponse

	# return HttpResponse(json.dumps(context))
	return JsonResponse(context, safe=False)


