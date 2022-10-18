from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.exceptions import BookCheckedOutException, BookCheckedInException
from books.models import Book
from books.permissions import IsStaffOrReadOnly
from books.serializers import BasicBookSerializer, FullBookSerializer


@permission_classes([IsStaffOrReadOnly])
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides `list`, `create`, `retrieve`, `update` and `destroy` 
    actions for books.
    """
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullBookSerializer
        return BasicBookSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'], 
        permission_classes=[IsAuthenticated], name='Check Out')
    def check_out(self, request, pk=None):
        """Check out a book."""
        book = self.get_object()
        serializer_context = {
            'request': request,
        }
        serializer = BookSerializer(book, context=serializer_context)
        
        if book.checked_out_by != None:
            raise BookCheckedOutException()
        book.checked_out_by = request.user
        book.save()
        return Response(serializer.data)

    @action(detail=True, methods=['post'], 
        permission_classes=[IsAuthenticated], name='Check In')
    def check_in(self, request, pk=None):
        """Check in a book."""
        book = self.get_object()
        serializer_context = {
            'request': request,
        }
        serializer = BookSerializer(book, context=serializer_context)

        if book.checked_out_by == None:
            raise BookCheckedInException()
        book.checked_out_by = None
        book.save()
        return Response(serializer.data)
