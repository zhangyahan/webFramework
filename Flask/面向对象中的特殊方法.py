

class Foo(object):

	def __init__(self):
		# self.storage = {}
		object.__setattr__(self, 'storage', {})

	def __setattr__(self, key, value):
		# print(self.storage)
		print(key, value, self.storage)


	def __getattr__(self, item):
		print(item)

	# pass

obj = Foo()
obj.xx = 123