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
    MEMBER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    STATUS = [
        (MEMBER, 'Пользователь'),
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор')
    ]

    role = models.CharField(choices=STATUS, max_length=9)
    age = models.IntegerField(null=True)
    # location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    location = models.ManyToManyField(Location)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
