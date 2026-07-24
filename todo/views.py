from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.contrib.auth.models import User
from todo.models import Todo, TodoList
from todo.serializers import TodoListSerializer, TodoSerializer, UserSerializer
from todo.permissions import IsOwnerOrReadOnlyForTodoDetails, IsOwnerOrReadOnly

@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "todolists": reverse("todolist", request=request, format=format),
        }
    )

class TodoListView(generics.RetrieveUpdateAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        todolist, _created = TodoList.objects.get_or_create(user=self.request.user)
        return todolist

class TodoView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        todolist, _created = TodoList.objects.get_or_create(user=self.request.user)
        return Todo.objects.filter(todo_list=todolist) # get_or_create for occasion when user trying to see all todos without getting TodoList in the first place
                                                       # maybe we can visit todolistview before todoview, with like redirect or something but it seems like extra work

    def perform_create(self, serializer):
        todolist, _created = TodoList.objects.get_or_create(user=self.request.user)
        serializer.save(todo_list=todolist)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnlyForTodoDetails]
    serializer_class = TodoSerializer 
    queryset = Todo.objects.all()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# there can be ViewSet rewrite on all others classes but I don't think it will be better, especially considering get_or_create difficulty
