from django.conf.urls import url

from . import views

def method_to_run(request):
    print "test"


urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.result),
]
