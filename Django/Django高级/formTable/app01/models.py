from django.db import models

# Create your models here.


class UserInfo(models.Model):
	username = models.CharField(max_length=16)
	password = models.CharField(max_length=10)

	def __str__(self):
		return self.username

	class Meta:
		db_table = "userinfo"


class City(models.Model):
	city_name = models.CharField(max_length=16, unique=True)

	def __str__(self):
		return self.city_name

	class Meta:
		db_table = "city_name"

