import threading
import time
from threading import local

obj = local()  # 

def task(i):
	obj.xxx = i
	time.sleep(1)
	print(obj.xxx, i)

for i in range(10):
	t = threading.Thread(target=task, args=(i,))
	t.start()