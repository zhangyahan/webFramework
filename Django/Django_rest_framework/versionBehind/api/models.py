from django.db import models

# Create your models here.

class UserGroup(models.Model):
	"""用户分组表"""
	title = models.CharField(max_length=32)


class Role(models.Model):
	"""角色表"""
	title = models.CharField(max_length=32)


class UserInfo(models.Model):
	"""用户信息表"""
	user_type_choices = (
			(1, '普通用户'),
			(2, 'VIP'),
			(3, 'SVIP'),
		)
	user_type = models.IntegerField(choices=user_type_choices)

	username = models.CharField(max_length=16, unique=True)
	password = models.CharField(max_length=64)

	group = models.ForeignKey("UserGroup")
	role = models.ManyToManyField("Role")


	def __str__(self):
		return self.username


class UserToken(models.Model):
	"""登录令牌表"""
	user = models.OneToOneField('UserInfo')
	token = models.CharField(max_length=64)

