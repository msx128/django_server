from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from todo.models import Todo, TodoList
from todo.serializers import TodoListSerializer, TodoSerializer
# Create your views here.def todo_list(request):

@csrf_exempt
def todolist_list(request):
    if request.method == "GET":
        todolist, _created = TodoList.objects.get_or_create(user=request.user)
        serializer = TodoListSerializer(todolist)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST": 
        data = JSONParser().parse(request)
        data['user'] = request.user.id

        todolist, _created = TodoList.objects.get_or_create(user=request.user)
        serializer = TodoListSerializer(todolist, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
         
@csrf_exempt
def todo_list(request): #I'm not sure why there this function we get out data from todolist_list or todo_detail
    if request.method == "GET": # this is redundant code 
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST": 
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        todo.delete()
        return HttpResponse(status=204)
