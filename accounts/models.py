from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ADMIN = 'admin'
    MANAGER = 'manager'
    GRAPHIC = 'graphic'
    WEB = 'web'
    DATABASE = 'database'

    TYPE_CHOICES = (
        (ADMIN, 'Admin',),
        (MANAGER, 'Manager',),
        (GRAPHIC, 'Graphic',),
        (WEB, 'Web',),
        (DATABASE, 'database',),
    )

    type = models.CharField(
        verbose_name='Type',
        max_length=255,
        default=ADMIN,
        choices=TYPE_CHOICES,
    )
