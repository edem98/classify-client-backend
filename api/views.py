from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClassifiedUserSerializer, CarSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import ClassifiedUser, Cars
import sklearn.externals
import joblib
from datetime import date, datetime


def user_exist(user_data):
    try:

        user = ClassifiedUser.objects.filter(email=user_data['email'])
        return len(user) > 0
    except Exception as e:
        print(e)

def predictict_category(user_data):
    # load the prediction model
    pickled_model = joblib.load('api/model.pkl')
    data = []
    data.append(int(user_data['gender']))
    # get age
    now = date.today()
    birth_day = datetime.strptime(user_data['birth_day'], '%Y-%M-%d')
    age = now.year - birth_day.year
    data.append(age)
    # format graduated
    if user_data['graduated'] == 'on':
        data.append(1.0)
    else:
        data.append(0.0)
    # format ever married
    if user_data['ever_married'] == 'on':
        data.append(1.0)
    else:
        data.append(0.0)
    #get profession
    data.append(float(user_data['profession']))
    # get work experience
    data.append(float(user_data['work_experience']))
    # set spending score
    data.append(0)
    # get family size
    data.append(float(user_data['family_size']))
    # set anonymized category
    data.append(0.0)
    # predict with the model
    return pickled_model.predict([data])


def get_cars(category):
    cars = Cars.objects.filter(category=category)
    return cars

def create_new_user(user_data):
    graduated = False
    ever_married = False

    if user_data['graduated'] == 'on':
        graduated = True
    if user_data['ever_married'] == 'on':
        ever_married = True


    new_user = ClassifiedUser(
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                gender=user_data['gender'],
                ever_married=ever_married,
                birth_day=user_data['birth_day'],
                graduated=graduated,
                profession=user_data['profession'],
                work_experience=user_data['work_experience'],
                spending_score=0,
                family_size=user_data['family_size'],
                anonymised_category=None,
                segmentation=None,
                )

    new_user.segmentation = user_data['segmentation']

    return new_user

def index(request):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = ClassifiedUser.objects.all()
    serializer_class = ClassifiedUserSerializer

    def create(self,request,*args,**kwargs):
        user_data = request.data
        user_data = user_data['data']
        category = predictict_category(user_data)
        category = category[0]
        if user_data['gender'] == '1':
            user_data['gender'] = 'MALE'
        elif user_data['gender'] == '0':
            user_data['gender'] = 'FEMALE'
        if category is not None:
            user_data['segmentation'] = category
            if user_exist(user_data):
                cars = get_cars(category)
                serializer = CarSerializer(cars,many=True)
                return Response(serializer.data)
            else:
                new_user = create_new_user(user_data)
                new_user.save()
                cars = get_cars(category)
                serializer = CarSerializer(cars,many=True)
                return Response(serializer.data)

        else:
            return Response([])


class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer