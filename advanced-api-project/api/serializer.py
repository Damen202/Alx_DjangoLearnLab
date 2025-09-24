from .models import Book
from rest_framework import serializers


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'title', 'year']

    def validate(self, data):
        if len(data)['year']:
            raise serializers.ValidationError("Year must not be in the future")


class Authorserializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username')

    
        