from django.shortcuts import render,redirect
from models import Quotes
from django.urls import reverse
from django.contrib import messages
from ..login_registration.models import User
# from models import User

def index(request):
    quotes = Quotes.objects.all().order_by('-id')
    users = User.objects.all()

    context = {
        "quotes":quotes,
        "users":users,
    }

    return render(request, 'quotes/index.html',context)

def add_quote(request):
    try:
        request.session['user']
        print request.session['user'], "this is the user"
        if request.method == "POST":
            result = Quotes.objects.add_quote(request.POST,request.session['user'])

            print 'result ==',result

            return redirect('index')
        else:
            quotes = Quotes.objects.all()

            print quotes,"These are the quotes"

            context = {

                "quotes":quotes
            }
    except:
        print "returning exception"
        return redirect('index')
    print "sending back to index"
    return render(request, 'quotes/index.html',context)
