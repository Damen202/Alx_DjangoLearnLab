from .models import Book
from rest_framework import serializers
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication must not be in the future")
        return value


class Authorserializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username')

    
        