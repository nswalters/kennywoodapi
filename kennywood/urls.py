from django.conf.urls import include
from django.urls import path
#from rest_framework import routers

from kennywoodapi.views import register_user, login_user

#router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
]
