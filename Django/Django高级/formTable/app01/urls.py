from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^register1/$', views.register1, name="register1"),

	# 使用form组件
	url(r'^register2/$', views.register2, name="register2"),
	
]