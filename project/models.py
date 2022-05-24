from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    budget = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=0.0)

    def __str__(self):
        return str(self.title)
