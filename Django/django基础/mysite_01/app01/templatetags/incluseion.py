from django import template

register = template.Library()

@register.inclusion_tag(filename='test.html')
def test(n):
    n = 