from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^(?P<version>[v1|v2]+)/user/$", views.UserView.as_view(), name="user"),  # 使用URL获取版本号
	url(r"^(?P<version>[v1|v2]+)/django/$", views.DjangoView.as_view(), name="django"),  # 使用URL获取版本号
]