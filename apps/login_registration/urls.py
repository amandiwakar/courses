from django.conf.urls import url,include
from . import views
from views import index, login, register, success, logout, delete
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register/',register, name='register'),
    url(r'^login/', login, name='login'),
    url(r'^success$', success, name='success'),
    # url(r'add/', include('apps.book_review.urls')),
    url(r'^logout/', logout, name='logout'),
    url(r'^delete/(?P<id>\d+)$', delete, name='delete'),
]
