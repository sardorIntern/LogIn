from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField()
    source = models.CharField(max_length=128)

    def __str__(self):
        return self.title


