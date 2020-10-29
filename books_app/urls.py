from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/add/', views.create_book),
    path('/<int:book_id>/', views.book_details),
    path('/<int:book_id>/like', views.like_book), 
    path('/<int:book_id>/unlike', views.unlike_book), 
    path('/<int:book_id>/update', views.update_book),
    path('/<int:book_id>/delete', views.delete_book),
    path('/user_favorites', views.user_favorites)
    
]