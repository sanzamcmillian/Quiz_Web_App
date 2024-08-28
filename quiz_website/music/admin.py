from django.contrib import admin

# Register your models here.
from django.contrib import admin
from music.models import Album

admin.site.register(Album)

# registration for other tables in your database