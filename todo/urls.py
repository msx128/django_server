from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from todo import views


router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")

urlpatterns = format_suffix_patterns([
    path("", views.api_root, name="root"),
    path("tdlst", views.TodoListView.as_view(), name="todolist"),
    path("td", views.TodoView.as_view(), name="tdl"),
    path("<int:pk>", views.TodoDetailView.as_view(), name="tododetail"),
])
urlpatterns += [
    path("", include(router.urls)),
]
