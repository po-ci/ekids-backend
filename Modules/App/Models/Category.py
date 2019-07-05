from django.db import models


class BaseManager(models.Manager):
    pass


class Category(models.Model):
    en = models.CharField(max_length=50, null=False, unique=True)
    es = models.CharField(max_length=50, null=False, unique=True)
    enDesc = models.CharField(max_length=150, null=False, unique=True)
    esDesc = models.CharField(max_length=150, null=False, unique=True)

    def __str__(self):
        return self.name
