from django.db import models


class BaseManager(models.Manager):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name
