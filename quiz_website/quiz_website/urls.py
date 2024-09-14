# quiz_website/urls.py

from django.urls import path
from quiz_website import views

urlpatterns = [
    path('', views.home, name='home'),
]