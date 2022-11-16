from datetime import date, timedelta
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import re
from django.db import models


def age_validators(value):
    age = (date.today() - value) // timedelta(days=365.2425)
    if age < 9:
        raise ValidationError("Регистрация возможно если вы старше 9 лет.")


def email_validators(value):
    if re.search('@rambler.ru', value):
        raise ValidationError(f"Регистрация в зоне rambler запрещена")


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
    birth_date = models.DateField(validators=[age_validators], null=True)
    email = models.EmailField(unique=True, validators=[email_validators])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
