import threading
import time
from threading import local

obj = local()  # 

def task(i):
	print(threading.get_ident(), i)

for i in range(10):
	t = threading.Thread(target=task, args=(i,))
	t.start()