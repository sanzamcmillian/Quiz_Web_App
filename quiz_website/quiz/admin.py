from django.contrib import admin
from .models import Leaderboard, QuizResult, UserResponse

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz_category', 'score', 'total_questions', 'date_taken')
    list_filter = ('quiz_category', 'date_taken')
    search_fields = ('user__username', 'quiz_category')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_score', 'rank')
    search_fields = ('user__username',)


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question_text', 'selected_option', 'correct_option', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('user__username', 'question_text')
