from django.contrib import admin
from .models import Leaderboard, QuizResult, UserResponse

admin.site.register(QuizResult)
admin.site.register(Leaderboard)
admin.site.register(UserResponse)