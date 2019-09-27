from books.models import Book
from books.serializers import BookSerializer
from rest_framework import permissions, viewsets
from books.permissions import IsStaffOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    """
    Provides `list`, `create`, `retrieve`, `update` and `destroy` 
    actions for books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)