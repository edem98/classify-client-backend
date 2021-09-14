from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClassifiedUserSerializer, CarSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import ClassifiedUser, Cars


def predictict_category(user_data):
    return 'B'

def get_cars(category):
    cars = Cars.objects.filter(category=category)
    return cars

def index(request):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = ClassifiedUser.objects.all()
    serializer_class = ClassifiedUserSerializer

    def create(self,request,*args,**kwargs):
        user_data = request.data
        user_data = user_data['data']
        print(user_data)
        category = predictict_category(user_data)

        if category is not None:
            cars = get_cars(category)
            serializer = CarSerializer(cars,many=True)
            return Response(serializer.data)

        else:
            return Response([])


class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer