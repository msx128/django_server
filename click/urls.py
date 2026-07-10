from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="button"),
    path("click", views.click ,name="click"),
]
