from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Default homepage route
    path('quiz/', include('quiz.urls')),  # Include the quiz app URLs
    path('api/', include('quiz.urls')),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]