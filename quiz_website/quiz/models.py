from django.db import models
from decimal import Decimal

class QuizResult(models.Model):
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Score: {self.score}%'