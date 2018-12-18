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
from django.core.validators import RegexValidator  # 自定义校验
from django.core.exceptions import ValidationError  # 错误类型

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
		widget=forms.PasswordInput(
			attrs={
				"class": "form-control",
			}, 
			render_value=True),  # 定义输入框类型
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
		widget=forms.PasswordInput(
			attrs={
				"class": "form-control",
			}, 
			render_value=True),  # 定义输入框类型
		error_messages={
				"min_length": "密码不能小于6位",
				"max_length": "密码最长不能大于10位",
				"required": "该字段不能为空",
			},  # error_message代表错误信息
		)


	email = forms.EmailField(
			label='邮箱',
			widget=forms.EmailInput(
					attrs={
						"class": "form-control",
					}),
			error_messages={
				"required": "该字段不能为空",
			}
		)

	phone = forms.CharField(
			label='手机号',
			max_length=11,
			min_length=11,
			# 自定义校验规则
			validators=[RegexValidator(r'^[0-9]+$', '请输入数字'),
						RegexValidator(r'^1[3-9][0-9]{9}+$', '必须以159开头')],
			widget=forms.TextInput(
					attrs={
						"class": "form-control",
					}
				),
			error_messages={
				"min_length": "手机号不符合规范",
				"max_length": "手机号不符合规范",
				"required": "该字段不能为空",
			}	
		)

	city = forms.ChoiceField(
			choices=(models.City.objects.all().values_list("id", "city_name"),),
			label="城市",
			initial=1,
			widget=forms.widgets.Select,) # 单选下拉框

	# 重写init方法
	def __init__(self, *args, **kwargs):
		super(RegForm, self).__init__(*args, **kwargs)
		# 每次加载时从数据库更新字段
		self.fields['city'].widget.choices = models.City.objects.all().values_list("id", "city_name")

	def clean_username(self):
		value = self.cleaned_data["username"]  # 获取每个字段的value(用户填写的)
		if '金瓶梅' in value:
			raise ValidationError('这个名字不符合社会主义核心价值观!')
		return value

	# 重写父类的clean方法
	def clean(self):
		# 此时通过校验的数据都保存在self.cleaned_data中
		passowrd = self.cleaned_data.get("password")
		re_password = self.cleaned_data.get('re_password')
		if passowrd != re_password:
			self.add_error('re_password', ValidationError('两次密码不一致'))
			raise ValidationError('两次密码不一致')
		else:
			return self.cleaned_data

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
			# password = form_obj.cleaned_data.get('password')
			# re_password = form_obj.cleaned_data.get('re_password')
			# 校验通过,将数据写进数据库
			# 所有的数据都在form_obj.cleaned_data里面是一个字典
			# models.UserInfo.objects.create(form_obj.cleaned_data)
			print(form_obj.cleaned_data)
		print(form_obj.errors)

	return render(request, 'register2.html', {"form_obj": form_obj})



