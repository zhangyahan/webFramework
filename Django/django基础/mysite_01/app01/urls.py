from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^yimi/', yimi),
    url(r'^xiaohei/', xiaohei),
]
