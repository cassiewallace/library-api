from django.db import models
from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    checked_out_by = serializers.HyperlinkedRelatedField(view_name='user-detail',
        queryset=User.objects.all(), allow_null=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'creator', 'checked_out_by']