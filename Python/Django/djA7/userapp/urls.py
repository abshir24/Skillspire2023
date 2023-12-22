from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.index),
    path(r'adduser', views.adduser),
    path(r'userinfo/<int:id>', views.displayuser)
]