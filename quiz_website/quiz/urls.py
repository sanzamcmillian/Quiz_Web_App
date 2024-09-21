from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.result_view, name='test'),
    path('view/<str:category>/', views.quiz_view, name='quiz_view'),
    path('result/', views.result_view, name='result'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
