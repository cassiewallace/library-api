from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'creator']