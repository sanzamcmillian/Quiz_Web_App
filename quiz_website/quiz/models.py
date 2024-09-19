# models.py
from django.db import models
from users.models import CustomUser

class QuizResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    quiz_score = models.FloatField() 

    def __str__(self):
        return f"{self.user.username} - {self.quiz_score}"


class Leaderboard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    total_score = models.FloatField(default=0)
    rank = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return f"{self.user.username} - Rank: {self.rank}, Score: {self.total_score}"
