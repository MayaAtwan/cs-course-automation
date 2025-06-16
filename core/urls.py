from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercises_list, name='exercises_list'),
    path('add/', views.exercises_add, name='exercises_add'),
    path('delete/<int:pk>/', views.exercises_delete, name='exercises_delete'),  
]
