from django.db import models


# Create your models here.
class Ad(models.Model):
    Id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    author_id = models.IntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField()
    category_id = models.IntegerField()


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    age = models.IntegerField()
    location_id = models.IntegerField()
