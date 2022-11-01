from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.CharField(max_length=255, default="user")
    age = models.IntegerField(null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
