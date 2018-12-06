import functools


def index(a1, a2):
	return a1 + a2


# 将第二个参数绑定到第一个函数的第一个参数上
new_func = functools.partial(index, 666)

ret = new_func(10)

print(ret)