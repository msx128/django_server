from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Counter(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="button_counter",
    )
    count = models.PositiveIntegerField(default=0)    
