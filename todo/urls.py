from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
    path("", views.todolist_list, name="todolist"),
    path("td", views.todo_list, name="skrr"),
    path("<int:pk>", views.todo_detail, name="detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
