from django.db import models

# Create your models here.



class FixedCharField(models.Field):
	"""
	自定义char类型的字段类
	"""

	def __init__(self, max_length, *args, **kwargs):
		self.max_length = max_length
		super(FixedCharField, self).__init__(max_length=max_length *args, **kwargs)

	def db_type(self, connection):
		"""
		限定生成数据库表的字段类型为char, 长度为max_length指定的值
		"""

		return 'char(%s)' % self.max_length


class Publish(models.Model):
	name = models.CharField(max_length=64, unique=True)
	address = models.CharField(max_length=128)

	class Meta:
		# 指定在数据库中表的名字
		db_table = 'Publish'
		
			