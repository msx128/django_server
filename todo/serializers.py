from rest_framework import serializers
from todo.models import Todo, TodoList

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "text", "complete"]
        read_only_fields = ["todo_list"]  

class TodoListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True, source="todo_set")

    class Meta:
        model = TodoList
        fields = ["id", "user", "title", "todos"]
