from django.db import models
from django.contrib.auth.models import User

from rest_framework import serializers

from books.models import Book


class BasicBookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'cover_image']

class FullBookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    checked_out_by = serializers.HyperlinkedRelatedField(view_name='user-detail',
        queryset=User.objects.all(), allow_null=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'owner', 'checked_out_by']
