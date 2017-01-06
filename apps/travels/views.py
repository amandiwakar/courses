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

def join_t(request,id):
    print request.session['user'],"This is the request"
    data = request.session['user']
    id = int(id)
    print id, "this is the travel ID"
    add_to_travel = Travels.objects.join_travel(data,id)
    return redirect('index')

def destination(request,id):
    id = int(id)

    one_entry = Travels.objects.get(id=id)
    print one_entry

    context = {

        "destination":one_entry
    }



    return render(request, 'travels/destination.html',context)
