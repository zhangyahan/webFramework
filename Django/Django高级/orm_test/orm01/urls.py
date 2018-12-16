from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^books/$', views.book, name='book'),
	url(r'^depts/$', views.dept, name='dept'),
]