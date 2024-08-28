# website/urls.py


from django.contrib import admin
from django.urls import path
from music.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('admin/', admin.site.urls),
 path('', home),
 path('about/', about),
 # Add URLs for other views here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
