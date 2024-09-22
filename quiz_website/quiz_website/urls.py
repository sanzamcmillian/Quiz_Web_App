from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_view, name='home'),  # Default homepage route
    path('quiz/', include('quiz.urls')),  # Include the quiz app URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('quiz_detail/', views.home_view, name='quiz_detail'),
    path('quiz_view/', views.quiz_view, name='quiz_view'),
    path('result/', views.result_view, name='result_view'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard_view'),
]