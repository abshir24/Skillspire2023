from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.home),
    path(r'coding-playlist/', views.coding),
    path(r'earth-playlist', views.earth)
]