from django.contrib import admin
from django.urls import path, include
from quiz import views  # Import the views from the quiz app if necessary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),  # Include all quiz-related URLs
    path('', views.home_view, name='home'),  # Your home view from quiz.views
]