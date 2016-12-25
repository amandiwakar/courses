from django.shortcuts import render, HttpResponse, redirect
import re

database = {


}
# Create your views here.

def index(request):
    return render(request, 'ninjas/index.html')

def ninjas(request):
    return render(request, 'ninjas/ninjas.html')

def color(request,color):
    context = {
        'turtle' : color,
    }

    tmnt = {

        'ninja':["red","blue","orange","purple"]
    }

    for val in tmnt.itervalues():
        for color_of_turtle in val:

            if color in val:
                return render(request, 'ninjas/whichninja.html', context)
            else:
                return render(request, 'ninjas/fox.html', context)













# from django.shortcuts import render
#
# # Create your views here.
# def index(request):
#     return render(request,'ninjaapp/index.html')
#
# def show(request, ninja_color):
#     turtle_options = {
#         'red':'ninjaapp/raphael.jpg',
#         'blue':'ninjaapp/leonardo.jpg',
#         'orange':'ninjaapp/michaelangelo.jpg',
#         'purple':'ninjaapp/donatello.jpg'
#     }
#     if ninja_color in turtle_options:
#         context = {
#             'image':turtle_options[ninja_color]
#         }
#     else:
#         context = {
#             'image':'ninjaapp/april.jpg'
#         }
#     """
#     A less concise version:
#     if ninja_color == 'red':
#         context= {
#             'image':'ninjaapp/raphael.jpg'
#         }
#     elif ninja_color == 'blue':
#         context= {
#             'image':'ninjaapp/leonardo.jpg'
#         }
#     elif ninja_color == 'purple':
#         context= {
#             'image':'ninjaapp/donatello.jpg'
#         }
#     elif ninja_color == 'orange':
#         context= {
#             'image':'ninjaapp/michaelangelo.jpg'
#         }
#     else:
#         context= {
#             'image':'ninjaapp/april.jpg'
#         }
#     """
#     return render(request,'ninjaapp/index.html',context)


# from django.conf.urls import url
# from . import views
# urlpatterns = [
#     url(r'^ninjas$', views.index, name = 'index'),
#     url(r'^ninjas/(?P<ninja_color>\w+)$', views.show, name = 'show')

#
# from __future__ import unicode_literals
#
# from django.apps import AppConfig
#
#
# class NinjaappConfig(AppConfig):
#     name = 'ninjaapp'
