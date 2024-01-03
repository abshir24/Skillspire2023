from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)