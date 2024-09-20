from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model

from django.db import models

class Types(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    question_type = models.ForeignKey(Types, on_delete=models.CASCADE, related_name='questions')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference the built-in User model
    quiz_score = models.FloatField() 

    def __str__(self):
        return f"{self.user.username} - {self.quiz_score}"


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference the built-in User model
    total_score = models.FloatField(default=0)
    rank = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return f"{self.user.username} - Rank: {self.rank}, Score: {self.total_score}"

