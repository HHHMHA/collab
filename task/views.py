from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .forms import TaskUpdateForm
from .models import Task


class TaskListView(ListView):
    model = Task
    paginate_by = 10
    queryset = Task.objects.all().order_by("deadline")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task_update_form.html'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
