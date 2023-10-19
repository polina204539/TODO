from django.urls import path
from todo import views

urlpatterns = [
    path('todo/', views.TodolistView.as_view()),
    path('todo/<int:id>', views.TodoDetailView.as_view()),
]