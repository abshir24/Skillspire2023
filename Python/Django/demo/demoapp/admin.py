from django.contrib import admin
from demoapp.models import User, Post

# Register your models here.
admin.site.register(User)
admin.site.register(Post)

# Super user info
# Email: test@test.com # Username: abshir24 # password: 123456