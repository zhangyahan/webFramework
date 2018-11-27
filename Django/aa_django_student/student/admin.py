from django.contrib import admin
from student import models
# Register your models here.

admin.site.register(models.Classes)
admin.site.register(models.Teachers)
admin.site.register(models.Student)
