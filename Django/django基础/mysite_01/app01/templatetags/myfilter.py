from django import template
register = template.Library()  # 创建对象


# 注册
@register.filter(name='sb')
def add_sb(arg):
    return "{} sb.".format(arg)


@register.filter(name='addstr')
def add_sb(arg, arg2):
    """
    第一个参数永远是管道符前面的那个变量
    :param arg:  管道前面那个变量
    :param arg2: 冒号后面引号里面的编程
    """
    return "{} {}.".format(arg, arg2)
