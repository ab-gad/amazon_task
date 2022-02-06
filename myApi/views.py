from django.shortcuts import render
from .serializers import IntakeSerializer, TraineeSerializer
from rest_framework import viewsets
from amazon.models import Intake, Trainee

# To create a function view here in our (api domain) we will use both api_view & response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# Notice >> Using ModelViewSet gives u a high lvl of abstraction, it handles all operations and endponints
# you will use one url, one view, and many endpoints r ready for u to use
# go to urls for more details     
class IntakeViewSet(viewsets.ModelViewSet):
    queryset =  Intake.objects.all()
    serializer_class = IntakeSerializer

class TraineeViewSet(viewsets.ModelViewSet):
    queryset =  Trainee.objects.all()
    serializer_class = TraineeSerializer


@api_view(['GET','POST'])
def traineeFBV(request):
    if request.method == 'GET':
        trainees = Trainee.objects.all()
        serializers = TraineeSerializer(trainees,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        serializers = TraineeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def traineeFBV_detail(request, pk):
    try:
        trainees = Trainee.objects.get(pk=pk)
    except Trainee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = TraineeSerializer(trainees)
        return Response(serializer.data)
  
    elif request.method == 'PUT':
        serializer = TraineeSerializer(trainees, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = TraineeSerializer(trainees,
                                           data=request.data,
                                           partial=True)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        trainees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)