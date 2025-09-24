from .models import Book, Author
from rest_framework import serializers
from datetime import datetime


class Bookserializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    publication_year = serializers.IntegerField()

    class Meta:
        model = Book
        fields = '__all__'


    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication must not be in the future")
        return value


class Authorserializer(serializers.ModelSerializer):
    books = Bookserializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

    
        