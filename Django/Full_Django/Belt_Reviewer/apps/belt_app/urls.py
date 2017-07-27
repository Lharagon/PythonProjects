from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^books$', views.books, name = 'my_books'),
    url(r'^register$', views.register, name = 'my_registration'),
    url(r'^login$', views.login, name = 'my_login'),
    url(r'^log_out$', views.log_out, name = 'my_log_out'),
    url(r'^add$', views.add, name = 'my_add'),
    url(r'^add_book$', views.add_book),
    url(r'^book_pro/(?P<id>\d+)$', views.book_pro, name = 'book_profile'),
    url(r'^add_review/(?P<id>\d+)$', views.add_review),
    url(r'^user_pro/(?P<id>\d+)$', views.user_pro, name = 'user_profile'),
    url(r'^delete/(?P<id>\d+)/(?P<bid>\d+)$', views.delete, name= 'delete_review')
]
