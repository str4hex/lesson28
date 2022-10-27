from rest_framework import serializers
from ads.models import Ad, Category, User
from user.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = User
        fields = ['first_name', 'location']


class AdsSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Ad
        fields = '__all__'
