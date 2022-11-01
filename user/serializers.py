from rest_framework import serializers
from user.models import User, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'lat', 'lng']


class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    location = LocationSerializer

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user
