from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from category.models import Category
from user.models import User


def name_length_validators(value):
    values = len(value)
    if values < 10:
        raise ValidationError(f"{value} not is length min 10 char")



# Create your models here.
class Ad(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, validators=[name_length_validators])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class Selection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='selections')
    name = models.CharField(max_length=100, unique=True)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = 'Подборка объявлений'
        verbose_name_plural = 'Подборки Объявлений'

    def __str__(self):
        return self.name
