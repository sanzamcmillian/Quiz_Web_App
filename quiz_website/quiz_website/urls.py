from django.contrib import admin
from django.urls import path, include
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Default homepage route
    path('quiz/', include('quiz.urls')),  # Include the quiz app URLs
    path('api/', include('quiz.urls')),
    path('api/register/', views.register_view, name='register'),
    path('api/login/', views.login_view, name='login'),
]