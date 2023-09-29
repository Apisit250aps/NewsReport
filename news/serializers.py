from rest_framework import serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Content
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'
