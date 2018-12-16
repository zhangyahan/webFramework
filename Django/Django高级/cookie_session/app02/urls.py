from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^home/$', views.home, name='home'),
	url(r'^login/$', views.login, name='login'),
	url(r'^loguot/$', views.logout, name='logout'),
	url(r'^userinfo/$', views.UserInfo.as_view(), name='userinfo'),
]