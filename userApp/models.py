from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'normal'),
      (2, 'admin')
    )
    user_type = models.PositiveSmallIntegerField(null=True, choices=USER_TYPE_CHOICES, default=1)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


    def __str__(self):
        return self.username

