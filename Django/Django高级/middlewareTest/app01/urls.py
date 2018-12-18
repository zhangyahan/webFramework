from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.app01_index, name="index"),

]
