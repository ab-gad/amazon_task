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
        User.objects.create_user(username=request.POST['first_name'], password=request.POST['password'], is_staff=True)
        return redirect(login) 

def login(request):
    if (request.method == 'GET'):
        return render(request,'login.html')
    else:
        user = myUsers.objects.all().filter(email=request.POST['email'], password=request.POST['password'])
        # user = myUsers.objects.all().filter(email<colName>=request.POST['email'<inputName>], password=request.POST['password'])
        authuser = authenticate(username = user[0].first_name, password=request.POST['password'])
        
        print(authuser, user[0].first_name)
        #username = user[0].first_name
        if (len(user) > 0 and authuser is not None):
            
            context = {}
            context['first_name'] = user[0].first_name
            context['last_name'] = user[0].last_name
            print(context)
            print(authuser)
            request.session['user'] = context
            
            authlogin(request, authuser)
            
            return redirect('/amazon/home/')
        else:
            context = {}
            context ['errmsg'] = 'inValid cred'
            return render(request, 'login.html', context)

# def checklogin(request):
#     if (request.method == 'POST'):
#         return redirect(home)

def home(request):
    try: 
        if(request.session['user'] is not None):
            return render(request,'home.html')
    except:
        return redirect(login)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def nav(request):
    return render(request, 'nav.html')

def create(request):
    if (request.method == 'GET'):
        return render(request, 'create.html')
    else:
        myUsers.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        context = {}
        context['msg'] = 'User has been Created Successfully'
        return render(request, 'create.html', context)

def read(request):
    if (request.method == 'GET'):
        return render(request, 'read.html')
    else:
        id = request.POST['id']
        if (id == '*'):
            allusers = myUsers.objects.all()
            context = {}
            context['allusers'] = allusers
            return render(request, 'read.html', context)
        else:
            try:
                selectedUser = myUsers.objects.get(id = request.POST['id'])
                print(selectedUser.first_name)
                context = {}
                context['selectedUser'] = selectedUser
                return render(request, 'read.html', context)
            except:
                context = {}
                context['msg'] = 'User You Try To Get Is Not Found'
                return render(request, 'read.html', context)

def update(request, id):
    if (request.method == 'GET'):
        selectedUser = myUsers.objects.get(id = id)
        context = {}
        print(selectedUser.first_name)
        context['selectedUser'] = selectedUser
        return render(request, 'update.html', context)
    else:
        myUsers.objects.filter(id=id).update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        context = {}
        context['msg'] = "User has been updated successfull"
        return render(request, 'update.html', context)

        
def delete(request, id):
    myUsers.objects.filter(id=id).delete()
    return redirect('/amazon/read/')

def logout(request):
    request.session.clear()
    return redirect(login)
