from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^student/$', views.Student),
	url(r'^studentclass/$', views.StudentsView.as_view())
]