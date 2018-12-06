import threading
import time


try:
	import greenlet
	get_ident = greenlet.getcurrent
except Exception as e:
	get_ident = threading.get_ident


class Local(object):

	DIC = {}

	def __getattr__(self, item):
		ident = get_ident()
		if ident in self.DIC:
			return self.DIC[ident].get(item)
		else:
			return None

	def __setattr__(self, key, value):
		ident = get_ident()
		if ident in self.DIC:
			self.DIC[ident][key] = value
		else:
			self.DIC[ident] = {key: value}


obj = Local()

def task(i):
	obj.xxx = i
	time.sleep(1)
	print(obj.xxx, i)

for i in range(10):
	t = threading.Thread(target=task, args=(i,))
	t.start()