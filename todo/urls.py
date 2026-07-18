from django.urls import path
from todo import views

urlpatterns = [
    path("", views.todolist_list, name="todolist"),
    path("<int:pk>", views.todo_detail, name="detail"),
]
