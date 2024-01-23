from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self) -> str:
        return str(self.username)
