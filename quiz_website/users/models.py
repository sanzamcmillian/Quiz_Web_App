from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(max_length=50, unique=True)

    # USERNAME_FIELD = "email"