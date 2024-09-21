from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
from django.db import models


class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_score = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.quiz_score}"


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.FloatField(default=0)
    rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Rank: {self.rank}, Score: {self.total_score}"
