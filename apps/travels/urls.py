from django.conf.urls import url
from . import views
from views import index, add_travel,destination,join_t
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_travel$',add_travel,name='add_travel'),
    url(r'^destination/(?P<id>\d+)$',destination,name='destination'),
    url(r'^join_t/(?P<id>\d+)$',join_t,name='join_t'),
    # url(r'login$', login, name='login'),
    # url(r'success$', success, name='success'),
    # url(r'logout$', logout, name='logout'),
    # url(r'delete/(?P<id>\d+)$', delete, name='delete'),
]
