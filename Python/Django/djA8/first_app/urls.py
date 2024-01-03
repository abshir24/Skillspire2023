# Inside first_project/first_app/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.allusers),
    path(r'users/new',views.userform),
    path(r'adduser',views.adduser),
    path(r'users/show/<int:id>',views.showuser, name="show-user"),
    path(r'users/edit/<int:id>',views.edituser, name="edit-user"),
    path(r'updateuser/<int:id>',views.updateuser, name="update-user"),
    path(r'users/delete/<int:id>',views.deleteuser, name="delete-user")
]