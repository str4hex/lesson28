import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from user.models import User, Location


class EmailValidators:

    def __init__(self, email):
        self.email = email

    def __call__(self, value):
        if re.search('@rambler.ru', value):
            raise ValidationError(f"Регистрация в зоне rambler запрещена")


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    location = LocationSerializer
    email = serializers.EmailField(
        validators=[EmailValidators([]), UniqueValidator(queryset=User.objects.all(), lookup='contains')])

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])

        user.save()

        return user
