from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^yimi/', views.yimi),
    url(r'^xiaohei/', views.xiaohei),
    url(r'^login/', views.login),
]
