from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IntakeViewSet, TraineeViewSet, traineeFBV, traineeFBV_detail

router  = DefaultRouter()

# Notice bc of using ModelViewSet , u have now more end points r ready to use
# api/trainee    >> list all data
# api/trainee/id >> retrieve specific traine
# u can make post requests to the same url 'api/trainee' with the required data to Create a trainee
# .. without handling this operation in views.py >>> NICE

router.register(r'intakes', IntakeViewSet, basename='intakes')
router.register(r'trainees', TraineeViewSet, basename='trainees')
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('traineeFBV/', traineeFBV),
    path('traineeFBV_detail/<pk>', traineeFBV_detail)
    
]