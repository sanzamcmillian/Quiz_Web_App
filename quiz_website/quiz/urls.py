# quiz/urls.py
from django.urls import path
from . import views
app_name = 'quiz'
 
urlpatterns = [
    path('', views.index_view, name='index'), 
    path('home/', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('quiz/view/', views.quiz_view, name='quiz_view'),
    path('result/', views.result_view, name='result'),
]
