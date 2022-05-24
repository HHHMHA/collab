from django.urls import path

from task.views import TaskListView, TaskUpdateView

app_name = "task"

urlpatterns = [
    path('', TaskListView.as_view(),  name='home'),
    path('update/<int:pk>', TaskUpdateView.as_view(),  name='update-task'),
]