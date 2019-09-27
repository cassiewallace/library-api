from django.contrib.auth.models import User, Group
from rest_framework import serializers
from books.models import Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    created_books = serializers.HyperlinkedRelatedField(many=True, 
        view_name='book-detail', read_only=True)
    checked_out_books = serializers.HyperlinkedRelatedField(many=True, 
        view_name='book-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'groups', 'created_books', 
            'checked_out_books']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']