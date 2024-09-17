from django.urls import path
from . import views
from .views import register_view

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('view/<str:category>/', views.quiz_view, name='quiz_view'),
    path('result/', views.result_view, name='result'),
    path('api/login/', views.login_view, name='login'),
    path('api/register/', views.register_view, name='register'),
    path('api/logout/', views.logout_view, name='logout'),
]
