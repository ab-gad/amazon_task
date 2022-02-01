from django.urls import path
from amazon.views import *


urlpatterns = [
    path('home/<name>', home),
    path('home/', home, name = 'home'),
    path('contact/', contact, name = 'contact'),
    path('about/', about, name = 'about'),
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    # path('checklogin/', checklogin, name = 'checklogin'),
]