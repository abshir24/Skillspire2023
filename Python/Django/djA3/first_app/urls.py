# Inside first_project/first_app/urls.py

from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.index),
    path(r'displayname', views.displayname),
    path(r'displayfood', views.displayfood),
    path(r'displayvacation', views.displayvacation)
]