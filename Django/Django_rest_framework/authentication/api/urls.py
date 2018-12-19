from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^auth/$', views.AuthView.as_view()),
	url(r'^order/$', views.OrderView.as_view()),
	url(r'^userinfo/$', views.UserInfo.as_view()),
]