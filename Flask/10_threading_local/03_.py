import threading
import time
import greenlet

DIC = {} 

def task(i):
	# ident = threading.get_ident()
	ident = greenlet.getcurrent()
	if ident in DIC:
		DIC[ident]['xxx'] = i
	else:
		DIC[ident] = {'xxx': i}

	time.sleep(2)
	print(DIC[ident]['xxx'], i)

for i in range(10):
	t = threading.Thread(target=task, args=(i,))
	t.start()