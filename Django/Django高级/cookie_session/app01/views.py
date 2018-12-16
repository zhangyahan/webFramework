from django.shortcuts import render, redirect, reverse
from functools import wraps
# Create your views here.



def wapper(func):
	@wraps(func)  # 装饰器修复技术
	def inner(request, *args, **kwargs):
		if request.get_signed_cookie('is_login', default=0, salt='~!@#$%^&*()_+') == '1':
			ret = func(request, *args, **kwargs)
			return ret
		else:
			next_path = request.path_info
			print(next_path)
			return redirect('/login/?next={}'.format(next_path))

	return inner


@wapper
def home(request):
	# # is_login = request.COOKIES.get('is_login', '')  # 从请求的cookie中获取is_login
	# is_login = request.get_signed_cookie('is_login', default=0, salt='~!@#$%^&*()_+')

	# if is_login:
	return render(request, 'home.html')
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
				ret = redirect('/home/')
			# ret.set_cookie(key='is_login', value=1)  # 设置cookie
			ret.set_signed_cookie('is_login', 1, salt='~!@#$%^&*()_+', )  # 设置加盐的cookie
			return ret
	
	return render(request, 'login.html')


def logout(request):
	ret = redirect(reverse('login'))
	ret.delete_cookie('is_login')
	return ret

