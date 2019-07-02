from django.db import models

# Create your models here.
class BaseManager(models.Manager):
    pass


class Mail(models.Model):
    sender = models.TextField()
    to = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField()
    objects = BaseManager()
