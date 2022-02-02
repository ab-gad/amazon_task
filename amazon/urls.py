from django.urls import path
from amazon.views import *


urlpatterns = [
    path('', home),
    path('home/', home, name = 'home'),
    path('contact/', contact, name = 'contact'),
    path('about/', about, name = 'about'),
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('create/', create, name = 'create'),
    path('read/', read, name = 'read'),
    path('update/<id>', update, name = 'update'),
    path('delete/<id>', delete, name = 'delete'),
    path('logout/', logout, name = 'logout'),
    path('createTrack/', createTrack, name = 'createTrack'),
    path('createTrainee/', createTrainee, name = 'createTrainee'),
    path('CreateIntake/', CreateIntake.as_view(), name = 'CreateIntake'),
    path('TrackList/', TrackList.as_view(), name = 'TrackList'),
    
    # path('checklogin/', checklogin, name = 'checklogin'),
]