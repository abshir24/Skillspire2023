from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Post(models.Model):
    name = models.CharField(max_length=200)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)