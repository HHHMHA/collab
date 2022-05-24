from django.contrib import admin

# Register your models here.
from project.models import Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project


admin.site.register(Project, ProjectAdmin)
