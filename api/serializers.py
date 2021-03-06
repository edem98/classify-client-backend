from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import ClassifiedUser, Cars


class ClassifiedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClassifiedUser
        fields = [
            'first_name','last_name',
            'email','gender','ever_married',
            'birth_day','graduated','profession',
            'work_experience', 'spending_score',
            'family_size', 'family_size', 'anonymised_category',
            'segmentation'
            ]

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ['brand','model','color','price','category','image']