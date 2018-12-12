from django.conf.urls import url
from home import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^students/$', views.StudentsView.as_view(), name='students'),
	# url(r'^teachers/$', views.TeachersView.as_view(), name='teachers'),
]