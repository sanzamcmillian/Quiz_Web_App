from django.db import models

# Create your models here.
from django.db import models
class User_Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    def __str__(self):
        return self.subject

   
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as necessary

    def __str__(self):
        return self.title