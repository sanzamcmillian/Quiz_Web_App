from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _


class QuizResult(models.Model):
    """Model to store the quiz results."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=False, default=0)
    total_questions = models.IntegerField(null=False, default=0)
    quiz_category = models.CharField(max_length=100, null=False, default="")
    date_taken = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username}'s result for {self.quiz_category}"


class UserResponse(models.Model):
    """Model to store user responses."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    selected_option = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)
    is_correct = models.BooleanField()
    
    def __str__(self):
        return f"{self.user.username}'s response to: {self.question_text}"


class Leaderboard(models.Model):
    """Model to show the leaderboard across the website"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.FloatField(default=0)
    rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Rank: {self.rank}, Score: {self.total_score}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        leaderboard = Leaderboard.objects.order_by('-total_score')
        for idx, entry in enumerate(leaderboard, start=1):
            if entry.rank != idx:
                entry.rank = idx
                entry.save()
