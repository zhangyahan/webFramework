#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-11 08:26:21
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$

from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/', views.login, name='login'),
	url(r'^login/', views.Login.as_view(), name='login'),
	url(r'^upload/', views.upload, name='upload'),
	url(r'^json', views.json_data, name='json'),
]