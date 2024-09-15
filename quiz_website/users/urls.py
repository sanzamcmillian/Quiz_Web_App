from django.urls import path, include
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework import routers

from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', TokenCreateView.as_view(), name='login'),
    path('logout/', TokenDestroyView.as_view(), name='logout'),
    ]