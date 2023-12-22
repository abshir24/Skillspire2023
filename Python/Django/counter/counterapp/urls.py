# Inside first_project/first_app/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index),
    path(r'addtwo', views.addtwo),
    path(r'reset', views.reset)
]