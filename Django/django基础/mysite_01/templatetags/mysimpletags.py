from django import template


register = template.Library()


@register.inclusion_tag('xxx.html')
def show_results(n):
	n = 1 if n < 