from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30, blank=True)
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=512, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    column_name = models.CharField(max_length=30)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.column_name
