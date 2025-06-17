from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercises_list, name='exercises_list'),
    path('add/', views.exercises_add, name='exercises_add'),
    path('edit/<int:pk>/', views.exercises_edit, name='exercises_edit'),
    path('delete/<int:pk>/', views.exercises_delete, name='exercises_delete'),
    path('assignments/', views.assignments_list, name='assignments_list'),
path('assignments/create/', views.create_assignment, name='create_assignment'),

    
]
