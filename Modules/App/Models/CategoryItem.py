from django.db import models
from .Category import Category


class BaseManager(models.Manager):
    pass


class CategoryItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    english = models.CharField(max_length=50, null=True)
    spanish = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to="images", max_length=100, null=True)
    audio = models.FileField(upload_to="audio", max_length=100, null=True)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.english
