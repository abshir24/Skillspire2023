from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    diet = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)