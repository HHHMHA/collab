from django.db import models


# Create your models here.

class Project(models.Model):
    budget = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=0.0)
