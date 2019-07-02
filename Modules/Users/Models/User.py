from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from .Avatar import Avatar


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    phone = models.TextField()
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE, related_name='avatar', null=True)


