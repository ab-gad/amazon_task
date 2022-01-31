from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request, name):
    context={}
    context['NAME'] = name
    return render(request,'home.html',context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def nav(request):
    return render(request, 'nav.html')