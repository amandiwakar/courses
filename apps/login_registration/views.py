from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from models import User

# Create your views here.

# Create your views here.
def index(request):

    users = User.objects.all()
    for user in users:
        print user.first_name, user.last_name

    return render(request, "login_registration/index.html", {'users':users})


def login(request):
    result = User.objects.validate_login(request)
    print 'processing login'
    print result
    if result[0] == False:
        print_messages(request, result[1])
        return redirect('/')

    return log_user_in(request, result[1])

def register(request):
    result = User.objects.validateReg(request)
    print "registering the user"
    print result[0]
    if result[0] == False:
        print result[0]
        print_messages(request, result[1])
        return redirect('/')

    return log_user_in(request, result[1])



def success(request):
    print 'processing success'
    if not 'user' in request.session:
        return redirect(reverse('index'))
    return render(request, 'login_registration/success.html')

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def log_user_in(request, user):
    request.session['user'] = {
    'id' : user.id,
    'first_name' : user.first_name,
    'last_name' : user.last_name,
    'email' : user.email,

    }
    context = {
    "user":request.session['user']
    }
    print 'processed log_user_in'
    # return redirect(reverse('add'))
    print 'sending user to add.html'
    return redirect(reverse('add_travel'),context)

def delete(request, id):
    u = User.objects.get(id=id).delete()
    print "deleted user", u
    return redirect(reverse('index'))

def logout(request):
    try:
        request.session.pop('user')
        return redirect('/')
    except:
        return render(request,'login_registration/index.html')
