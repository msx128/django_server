from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from todo.models import Todo, TodoList
from todo.serializers import TodoListSerializer, TodoSerializer
# Create your views here.def todo_list(request):

@api_view(["GET", "POST"])
def todolist_list(request, format=None):
    if request.method == "GET":
        todolist, _created = TodoList.objects.get_or_create(user=request.user)
        serializer = TodoListSerializer(todolist)
        return Response(serializer.data)

    elif request.method == "POST": 
        data = JSONParser().parse(request)
        data['user'] = request.user.id # can't just do TodoListSerializer(data=request.data)

        todolist, created = TodoList.objects.get_or_create(user=request.user)
        serializer = TodoListSerializer(todolist, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            c_status = status.HTTP_201_CREATED if created else status.HTTP_200_OK
            return Response(serializer.data, status=c_status)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
@api_view(["GET", "POST"])
def todo_list(request, format=None): 
    todolist, _created = TodoList.objects.get_or_create(user=request.user)
    if request.method == "GET": 
        todos = Todo.objects.filter(todo_list=todolist)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == "POST": 
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(todo_list=todolist)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def todo_detail(request, pk, format=None):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
