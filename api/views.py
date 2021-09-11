from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClassifiedUserSerializer, CarSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import ClassifiedUser, Cars

class UserViewSet(viewsets.ModelViewSet):
    queryset = ClassifiedUser.objects.all()
    serializer_class = ClassifiedUserSerializer

    def create(self,request,*args,**kwargs):
        user_data = request.data
        serializer = ClassifiedUserSerializer(user_data)
        return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer