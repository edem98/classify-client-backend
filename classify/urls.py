from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from api.views import UserViewSet, CarViewSet, index
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)