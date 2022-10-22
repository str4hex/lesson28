from django.db import models

# Create your models here.
from django.db import models


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    age = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)




# Create your models here.
