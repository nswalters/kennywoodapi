from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from kennywoodapi.models import *
from kennywoodapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'areas', ParkAreaViewset, 'parkarea')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
]
