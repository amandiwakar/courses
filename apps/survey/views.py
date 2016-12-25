from django.shortcuts import render, HttpResponse, redirect
import datetime
import random,string
# Create your views here.
def index(request):

    # try:
    #     name = request.session['name']
    #     email = request.session['email']
    # except:
    #     name = 'nothing'
    #     email = 'nothing'


    # return HttpResponse('<h1> Hello there world</h1>')
    return render(request, 'survey/index.html')

def result(request):
    # name = request.session['name']
    # email = request.session['email']

    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']
    request.session['dojo'] = request.POST['dojo']
    request.session['lang'] = request.POST['lang']
    context = {

        "name": request.session['name'],
        "email": request.session['email'],
        "dojo": request.session['dojo'],
        "lang": request.session['lang']
    }
    # return redirect('/results')
    return render(request, 'survey/result.html',context)

# def results(request):
#     return render(request, 'survey/result.html')
