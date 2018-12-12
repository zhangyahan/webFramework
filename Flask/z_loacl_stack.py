# 获取线程的唯一标识
from threading import get_ident
# 获取携程的唯一标识
from greenlet import getcurrent as get_ident


class Local(object):

	def __init__(self):
		object.__setattr__(self, 'storage', {})

	def __setattr__(self, key, value):
		ident = get_ident()
		if ident not in self.storage:
			self.storage[ident] = {key: value}
		else:
			self.storage[ident][key] = value

	def __getattr__(self, item):
		ident = get_ident()
		if ident in self.storage:
			return self.storage[ident].get(item)
		else:
			return None