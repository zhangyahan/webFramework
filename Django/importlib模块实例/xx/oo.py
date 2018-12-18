

NAME = 'oo.py'

class Person(object):
	def __init__(self, name):
		self.name = name

	def dream(self):
		print('{}在做美梦'.format(self.name))