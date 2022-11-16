from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, StepValueValidator
from django.db import models


def value_size_text_validators(value):
    values = len(value)
    if values < 5 or values > 10: raise ValidationError(f'{value} is not text 5 charfields and max 10',
                                                        params={'value': value},)


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=10, validators=[value_size_text_validators], unique=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
