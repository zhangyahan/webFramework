from redis_demo import RedisHelper

# 订阅者
obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
	msg = redis_sub.parse_response()
	print(msg)