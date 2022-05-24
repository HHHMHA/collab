from django.db import models


# Create your models here.
from task.models import Task


class Comment(models.Model):
    comment = models.TextField(null=True, blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
