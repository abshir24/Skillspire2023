from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.index),
    path(r'register', views.register),
    path(r'login', views.login),
    path(r'newsfeed', views.newsfeed),
    path(r'addpost', views.addpost),
    path(r'logout', views.logout)
]