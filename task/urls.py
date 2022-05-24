from django.urls import path

from task.views import TaskListView, TaskDetailView, TaskUpdateView

app_name = "task"
urlpatterns = [
    path('tasks/', TaskListView.as_view(),  name='task-list'),
    path('task-detail/<int:pk>', TaskDetailView.as_view(),  name='task-detail'),
    path('task-update/<int:pk>', TaskUpdateView.as_view(),  name='update-task'),
]