from django.shortcuts import render, redirect
from models import Reviews
from django.urls import reverse
from django.contrib import messages
from ..login_registration.models import User

# Create your views here.


def index(request):
    reviews = Reviews.objects.all()
    users = User.objects.all()

    for review in reviews:
        print review.title, review.reviewer

    for user in users:
        print user.first_name,user.last_name

    last_three = Reviews.objects.all().order_by('-id')[:3]



    context = {
        "reviews":reviews,
        "users":users,
    }
    return render(request, 'book_review/index.html',context)

def add(request):
        # for review in reviews:
        #     print review.title, review.author
        # users = User.objects.all()
        # for user in users:
        #     print user.first_name, user.last_name
    try:
        request.session['user']
        if request.method == "POST":
            result = Reviews.objects.add_book_review(request.POST,request.session['user'])
            print 'result ==',result

            return redirect('index')

        else:

            last_three = Reviews.objects.all().order_by('-id')[:3]

            print last_three, "last three reviews by GET"

            context = {

                "last_three":last_three,
            }
    except:
        return redirect('index')




    print 'processing book add'

    return render(request, 'book_review/add.html',context)
