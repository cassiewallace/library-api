from django.shortcuts import render
from rest_framework import viewsets
from .models import Books
from .serializers import BooksSerializer


class BooksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer