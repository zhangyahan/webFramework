from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$', views.student),
    url(r'^add/$', views.addStudent),
    url(r'^del/$', views.delStudent),

]