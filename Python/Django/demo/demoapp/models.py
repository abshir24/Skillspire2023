from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    password = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

class Post(models.Model):
    post = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)