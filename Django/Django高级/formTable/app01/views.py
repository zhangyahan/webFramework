from django.shortcuts import render, HttpResponse, redirect, reverse
from . import models
# Create your views here.


def register1(request):
	if request.method == "GET":
		return render(request, 'register1.html')
	else:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		if username == 'zyh' and password == '123456':
			return HttpResponse('登录成功')
		return redirect(reverse("register1"))



# Django-Form组件的使用
from django import forms


class RegForm(forms.Form):
	username = forms.CharField(
		max_length=16, 
		label="用户名",
		error_messages={
				"max_length": "账号不能大于16位",
				"required": "该字段不能为空",
			},
		widget=forms.widgets.TextInput(attrs={
				"class": "form-control",
			})
		)

	password = forms.CharField(
		label="密码", 
		min_length=6,  # min_lenth代表不能小于6位
		max_length=10,
		widget=forms.PasswordInput(attrs={
			"class": "form-control",
			}, render_value=True),  # 定义输入框类型
		error_messages={
				"min_length": "密码不能小于6位",
				"max_length": "密码最长不能大于10位",
				"required": "该字段不能为空",
			},  # error_message代表错误信息
		)

	re_password = forms.CharField(
		label="确认密码", 
		min_length=6,  # min_lenth代表不能小于6位
		max_length=10,
		widget=forms.PasswordInput(attrs={
			"class": "form-control",
			}, render_value=True),  # 定义输入框类型
		error_messages={
				"min_length": "密码不能小于6位",
				"max_length": "密码最长不能大于10位",
				"required": "该字段不能为空",
			},  # error_message代表错误信息
		)


	# email = forms.EmailField()
	# gender = forms.ChoiceField(
	# 		choices=((1, "男"), (2, "女"), (3, "保密"),),
	# 		label="性别",
	# 		initial=3,
	# 		widget=forms.widgets.RadioSelect,  # 枚举
	# 	)
	# hobby = forms.ChoiceField(
	# 		choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
	# 		label="爱好",
	# 		initial=3,
	# 		widget=forms.widgets.Select,  # 单选下拉框
	# 	)
	# hobby2 = forms.MultipleChoiceField(
	# 		choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
	# 		label="爱好",
	# 		initial=[1, 3],
	# 		widget=forms.widgets.SelectMultiple,  # 多选下拉框
	# 	)
	# keep = forms.ChoiceField(
	# 		label="是否记住密码",
	# 		initial="checked",
	# 		widget=forms.widgets.CheckboxInput,   # 单选checkbox
	# 	)
	# hobby3 = forms.MultipleChoiceField(
	# 	choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
	# 	label="爱好",
	# 	initial=[1, 3],
	# 	widget=forms.widgets.CheckboxSelectMultiple(attrs={
	# 		"class": "c1",  # 定义标签的类属性
	# 	}),  # 多选checkbox
	# )

def register2(request):
	form_obj = RegForm()
	if request.method == "POST":
		form_obj = RegForm(request.POST)
		# 让form帮我们做校验
		if form_obj.is_valid():
			password = form_obj.cleaned_data.get('password')
			re_password = form_obj.cleaned_data.get('re_password')
			# 校验通过,将数据写进数据库
			# 所有的数据都在form_obj.cleaned_data里面是一个字典
			# models.UserInfo.objects.create(form_obj.cleaned_data)
			print(form_obj.cleaned_data)
			pass

	return render(request, 'register2.html', {"form_obj": form_obj})

