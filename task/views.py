from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from .forms import TaskUpdateForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    queryset = Task.objects.all().order_by("deadline")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task_update_form.html'
