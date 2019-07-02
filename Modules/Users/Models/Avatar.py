from django.db import models


class BaseManager(models.Manager):
    pass


class Avatar(models.Model):
    image = models.ImageField(upload_to="avatars", max_length=100)
    objects = BaseManager()
