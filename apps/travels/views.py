from django.shortcuts import render,redirect
from models import Travels
from django.urls import reverse
from django.contrib import messages
from ..login_registration.models import User
# from models import User

def index(request):
    travels = Travels.objects.all().order_by('-id')
    users = User.objects.all()

    context = {
        "travels":travels,
        "users":users,
    }

    return render(request, 'travels/index.html',context)

def add_travel(request):
    try:
        request.session['user']
        print request.session['user'], "this is the user"
        if request.method == "POST":
            result = Travels.objects.add_travel(request.POST,request.session['user'])

            print 'result ==',result

            return redirect('index')
        else:
            travels = Travels.objects.all()

            print travels,"These are the travels"

            context = {

                "travels":travels
            }
    except:
        print "returning exception"
        return redirect('index')
    print "sending back to index"
    return render(request, 'travels/add_travel.html',context)

def destination(request,id):



    destination = Travels.objects.get(id=id)

    for destination in destination:
        print destination

    print destination

    return render(request, 'travels/destination.html')
