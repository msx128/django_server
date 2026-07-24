from rest_framework import serializers
from todo.models import Todo, TodoList
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "text", "complete", "created"]
        read_only_fields = ["todo_list"]  

class TodoListSerializer(serializers.ModelSerializer):
    todo_set = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Todo.objects.all()
    )
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = TodoList
        fields = ["id", "user", "title", "todo_set"]

class UserSerializer(serializers.ModelSerializer):
    todolist = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    class Meta:
        model = User
        fields = ["id", "username", "todolist"]
        
