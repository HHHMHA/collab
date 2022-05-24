from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from .forms import TaskUpdateForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = 'home.html'

    def get_queryset(self):
        qs = super(TaskListView, self).get_queryset()
        qs.filter(assignee=self.request.user).order_by('deadline')
        return qs


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task_update_form.html'

    def get_queryset(self):
        qs = super(TaskUpdateView, self).get_queryset()
        qs.filter(assignee=self.request.user)
        return qs
