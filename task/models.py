from django.db import models

# Create your models here.
from django.urls import reverse

from accounts.models import User
from project.models import Project


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.assignee.id, filename)


class Task(models.Model):
    PENDING = 'P'
    FEEDBACK = 'F'
    COMPLETED = 'C'

    STATUS_TYPE_CHOICES = (
        (PENDING, 'Pending',),
        (FEEDBACK, 'Feedback',),
        (COMPLETED, 'Completed',),

    )
    title = models.CharField(max_length=255, null=True, blank=False)
    description = models.CharField(max_length=255, null=True, blank=False)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=1, default=PENDING)
    deadline = models.DateField()
    upload = models.FileField(upload_to=user_directory_path)
    dependencies = models.ManyToManyField("self")
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('task:task-detail', kwargs={'pk': self.pk})
