from django.contrib import admin
from .models import Leaderboard, QuizResult

admin.site.register(QuizResult)
admin.site.register(Leaderboard)