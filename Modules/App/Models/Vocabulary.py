from django.db import models
from .Category import Category


class BaseManager(models.Manager):
    pass


class Vocabulary(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    en = models.CharField(max_length=50, null=True)
    es = models.CharField(max_length=50, null=True)
    img = models.ImageField(upload_to="images", max_length=100, null=True)
    snd = models.FileField(upload_to="audio", max_length=100, null=True)
    col = models.CharField(max_length=30)

    def __str__(self):
        return self.en
