from django.contrib import admin

# Register your models here.
from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    model = Task
    order = ["deadline"]


admin.site.register(Task, TaskAdmin)
