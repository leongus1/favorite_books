from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('check_log/', views.check_log),
    path('register/', views.register),
    path('logout', views.logout),
]