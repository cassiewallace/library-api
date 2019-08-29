from books.models import Book
from books.serializers import BookSerializer
from rest_framework import generics


class BookList(generics.ListCreateAPIView):
    """ List all books or create a new book. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update, or delete a book. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer