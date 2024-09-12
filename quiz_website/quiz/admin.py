from django.contrib import admin

# Register your models here.
from django.contrib import admin
from quiz.models import Quiz

admin.site.register(Quiz)

# registration for other tables in your database
