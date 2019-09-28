from books.models import Book
from books.permissions import IsStaffOrReadOnly
from books.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import permission_classes


@permission_classes([IsStaffOrReadOnly])
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides `list`, `create`, `retrieve`, `update` and `destroy` 
    actions for books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)