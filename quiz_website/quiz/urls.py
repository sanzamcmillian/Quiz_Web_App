from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view),
    path('', views.home_view, name='home'),
    path('view/<str:category>/', views.quiz_view, name='quiz_view'),
]
