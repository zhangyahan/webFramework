from django import template

# 生成一个注册实例,必须是register
register = template.Library()

@register.filter(name='myfilter')
def myfilter(value, arg):
	return "{} {}".format(value, arg)


@register.simple_tag(name='mysiple')
def mysimple(*args):
	args_list = list(args)
	return ",".join(args_list)


@register.inclusion_tag('inclusion.html')
def myinclusion(n):
	n = 1 if n < 1 else int(n)
	data = ['第{}项'.format(i) for i in range(1, n+1)]
	return {'data': data}
