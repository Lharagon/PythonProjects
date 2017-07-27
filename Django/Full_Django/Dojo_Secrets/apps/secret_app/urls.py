from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^log_out$', views.log_out),
    url(r'^post$', views.post),
    url(r'^like/(?P<sid>\d+)/(?P<uid>\d+)$', views.like),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'dell'),
    url(r'^popular$', views.popular, name="pop")
]