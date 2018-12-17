from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^serialize/$', views.serialize, name='serialize'),
	url(r'^sweetalert/', views.sweetalert, name='sweetalert'),
]