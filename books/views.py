from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from books.models import Book
from books.permissions import IsStaffOrReadOnly
from books.serializers import BookSerializer


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

    @action(detail=True, methods=['post'], 
        permission_classes=[IsAuthenticated], name='Check Out')
    def check_out(self, request, pk=None):
        """Check out a book."""
        book = self.get_object()

        book.checked_out_by = request.user
        book.save()

        return Response({'status': 'checked out'})

    @action(detail=True, methods=['post'], 
        permission_classes=[IsAuthenticated], name='Check In')
    def check_in(self, request, pk=None):
        """Check in a book."""
        book = self.get_object()

        book.checked_out_by = None
        book.save()

        return Response({'status': 'checked back in'})