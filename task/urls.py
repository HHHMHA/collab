from django.urls import path

from task.views import TaskListView, TaskUpdateView

app_name = "task"
urlpatterns = [
    path('tasks/', TaskListView.as_view(),  name='task-list'),
    path('task-update/<int:pk>', TaskUpdateView.as_view(),  name='update-task'),
]