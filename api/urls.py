from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('index/', router.urls),
]
