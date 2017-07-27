from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^(?P<id>\d+)/add_project$', views.add_p, name = "add_pro"),
    url(r'^adding_proj/(?P<id>\d+)$', views.adding_proj),
    url(r'^client/add$', views.add_c, name = "add_clie"),
    url(r'^adding_clie$', views.adding_clie),
    url(r'^client/(?P<id>\d+)$', views.client_pro, name = "client_pro"),
    url(r'^projects/(?P<id>\d+)$', views.project_pro, name = "project_pro")
]