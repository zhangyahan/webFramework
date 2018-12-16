from django.shortcuts import render, redirect, reverse
from django.views import View
from functools import wraps
# Create your views here.



def wapper(func):
	@wraps(func)  # 装饰器修复技术
	def inner(request, *args, **kwargs):
		if request.session.get('is_login', '') == '1':  # 获取session
			ret = func(request, *args, **kwargs)
			return ret
		else:
			next_path = request.path_info
			print(next_path)
			return redirect('/app02/login/?next={}'.format(next_path))

	return inner


@wapper
def home(request):
	# # is_login = request.COOKIES.get('is_login', '')  # 从请求的cookie中获取is_login
	# is_login = request.get_signed_cookie('is_login', default=0, salt='~!@#$%^&*()_+')

	# if is_login:
	context = {}

	username = request.session.get('username', '')

	context['username'] = username
	return render(request, 'app02/home.html', context)
	# else:
	# 	return redirect(reverse('login'))


def login(request):
	print(request.path_info)
	print(request.get_full_path())
	if request.method == "POST":
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		next_path = request.GET.get('next')
		if username == 'zyh' and password == '123456':
			if next_path:
				ret = redirect(next_path)  # 创建一个请求对象
			else:
				ret = redirect('/app02/home/')

			request.session['is_login'] = '1'  # 设置session
			request.session['username'] = username
			return ret
	
	return render(request, 'app02/login.html')


def logout(request):
	request.session.flush()  # 删除session和cookie
	request.session.delete()  # 只删除session
	return redirect(reverse('login'))

# Django提供的工具, 把函数装饰器变成方法装饰器
from django.utils.decorators import method_decorator

@method_decorator(wapper, name='get')  # 给类加装饰器,必须给name参数
class UserInfo(View):

	@method_decorator(wapper)  # 如果想给类中所有方法加装饰器,可以直接给disoatch方法加,dispatch为最先执行的方法
	def dispatch(self, request, *args, **kwargs):
		return super(UserInfo, sefl).dispatch(request, *args, **kwargs)

	# @method_decorator(wapper)  # 给类方法加装饰器
	def get(self, request):
		return render(request, 'app02/userinfo.html')

