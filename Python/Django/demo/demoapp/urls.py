from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.home),
    path(r'allposts',views.allposts),
    path(r'addpost',views.addpost),
    path(r'register',views.register),
    path(r'update',views.update),
    path(r'coding-playlist/', views.coding),
    path(r'earth-playlist', views.earth)
]