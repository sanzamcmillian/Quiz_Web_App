from django.urls import path
from . import views

urlpatterns = [
    path('view/<str:category>/', views.quiz_view, name='quiz_view'),
    path('result/<int:result_id>/', views.result_view, name='result_view'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard_view'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
