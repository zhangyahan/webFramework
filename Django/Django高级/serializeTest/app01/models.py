from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=16)
	age = models.SmallIntegerField()

	def __str__(self):
		return self.name

	class Mate:
		db_table = 'person'