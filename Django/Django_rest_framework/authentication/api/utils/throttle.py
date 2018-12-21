from rest_framework.throttling import BaseThrottle, SimpleRateThrottle

"""
import time
VISIT_RECORD = {}

class VisitThrottle(BaseThrottle):

	def __init__(self):
		self.history = None

	def allow_request(self, request, view):
		# 获取用户ip
		# remote_addr = request._request.META.get("REMOTE_ADDR")
		# remote_addr = request.META.get("REMOTE_ADDR")
		remote_addr = self.get_ident()  # 使用父类的方法获取唯一标识
		stime = time.time()
		if remote_addr not in VISIT_RECORD:
			VISIT_RECORD[remote_addr] = [stime,]
			return True

		history = VISIT_RECORD.get(remote_addr)
		self.history = history  # 将当前用户的访问列表赋值给self.history

		while history and history[-1] < stime - 60:
			# 如果history中有值和history的最早一次访问记录比当前时间-60秒小, 将history的-1pop
			history.pop()

		if len(history) < 3:
			history.insert(0, stime)
			return True
		# return True  # 表示可以访问
		# return False  # 表示访问频率太高,被限制

	def wait(self):
		# 还需要等多少秒可以访问
		s_time = time.time() 
		return 60 - (s_time-self.history[-1])
"""


class VisitThrottle(SimpleRateThrottle):
	scope = "zyh"  # key

	def get_cache_key(self, request, view):
		return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
	scope = "zyhuser"  # key

	def get_cache_key(self, request, view):
		return request.user.username
