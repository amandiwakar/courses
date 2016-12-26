from django.conf.urls import url
from . import views
from views import index, add_quote
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_quote$',add_quote,name='add_quote'),
    # url(r'login$', login, name='login'),
    # url(r'success$', success, name='success'),
    # url(r'logout$', logout, name='logout'),
    # url(r'delete/(?P<id>\d+)$', delete, name='delete'),
]
