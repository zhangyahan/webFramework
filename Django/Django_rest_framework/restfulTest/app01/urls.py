from django.conf.urls import url
from . import views

urlpatterns = [
	
	# url(r'^get_user', views.get_user, name='get_user'),
	# url(r'^add_user', views.add_user, name='add_user'),
	# url(r'^up_data_user', views.up_data_user, name='up_data_user'),
	# url(r'^del_user', views.del_user, name='del_user'),

	# url(r"^user", views.UserView.as_view(), name="user"),





	# django restful
	url(r"^user/", views.UserView.as_view(), name="user"),

]