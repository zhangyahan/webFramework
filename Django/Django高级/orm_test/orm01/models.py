from django.db import models

# Create your models here.




class Employee(models.Model):
	name = models.CharField(max_length=32)
	age = models.SmallIntegerField()
	salary = models.DecimalField(max_digits=10, decimal_places=2)
	province = models.CharField(max_length=32)
	department = models.ForeignKey('Department', null=True) 

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'employee'


class Department(models.Model):
	name = models.CharField(max_length=32)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'department'



class Author(models.Model):
	name = models.CharField(max_length=32)
	book = models.ManyToManyField(to='Book')

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'author'



class Book(models.Model):
	title = models.CharField(max_length=32)

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'book'














