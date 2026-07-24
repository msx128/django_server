from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoList(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ["user"]
    
class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.TextField()
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return str(self.id)
