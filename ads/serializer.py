from rest_framework import serializers
from ads.models import Ad, Category, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']


class AdsSerializer(serializers.ModelSerializer):

    author = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Ad
        fields = '__all__'