from books.models import Book
from books.serializers import BookSerializer
from rest_framework import generics, permissions
from books.permissions import IsOwnerOrReadOnly


class BookList(generics.ListCreateAPIView):
    """ List all books or create a new book. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update, or delete a book. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]