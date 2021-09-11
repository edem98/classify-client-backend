from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import ClassifiedUser, Cars

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',]


class ClassifiedUserSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ClassifiedUser
        fields = [
            'user','first_name','last_name',
            'email','gender','ever_married',
            'birth_day','graduated','profession',
            'work_experience', 'spending_score',
            'family_size', 'family_size', 'anonymised_category',
            'segmentation'
            ]

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ['brand','model','color','image']