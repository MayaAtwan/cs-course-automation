from django.urls import path
from . import views

urlpatterns = [
  path('exercises/', views.exercises_list, name='exercises_list'),
  path('exercises/add/',   views.exercises_add,  name='exercises_add'),
  # … later: edit, delete, assignments URLs …
]
