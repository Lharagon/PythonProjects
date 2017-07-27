from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^courses/comments/(?P<id>\d+)$', views.comments),
    url(r'^removing$', views.removing),
    url(r'^post$', views.post)
]