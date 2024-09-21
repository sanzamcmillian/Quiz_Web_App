from django.contrib import admin
from django.urls import path, include
from quiz.views import index_view, LoginView, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),  # Index before login
    path('quiz/', include('quiz.urls', namespace='quiz')),  # Include quiz app URLs
    path('login/', LoginView.as_view(), name='login'),  # Default login view
    path('home/', home_view, name='home'),

]
