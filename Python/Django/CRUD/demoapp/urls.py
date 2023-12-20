from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.home),
    path(r'addpost', views.addpost),
    path(r'edit/<int:id>', views.edit),
    path(r'editpost/<int:id>', views.edit),
    path(r'delete/<int:id>', views.delete) 
]