from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import myUsers
from django.contrib.auth.models import User #auth user table in DB
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout

# Create your views here.
def register(request):
    context = {}
    if (request.method == 'GET'):
        return render(request, 'register.html', context)
    else:
        myUsers.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])

        # NOTICE using create_user or create_superuser when dealing with User model
        User.objects.create_user(username=request.POST['first_name'], is_staff=True)
        return redirect(login) 

def login(request):
    if (request.method == 'GET'):
        return render(request,'login.html')
    else:
        user = myUsers.objects.all().filter(email=request.POST['email'], password=request.POST['password'])
        # user = myUsers.objects.all().filter(email<colName>=request.POST['email'<inputName>], password=request.POST['password'])
        
        #username = user[0].first_name
        if (len(user) > 0):
            
            context = {}
            context['first_name'] = user[0].first_name
            context['last_name'] = user[0].last_name

            print(context)
            return redirect('/amazon/home/', context)
        else:
            context = {}
            context ['errmsg'] = 'inValid cred'
            return render(request, 'login.html', context)

# def checklogin(request):
#     if (request.method == 'POST'):
#         return redirect(home)

def home(request, name = ""):
    # context={}
    # context['NAME'] = name
    return render(request,'home.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def nav(request):
    return render(request, 'nav.html')

