from django.contrib.auth.models import User, Group

from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Provides `list`, `create`, `retrieve`, `update`, and `destroy` 
    actions for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides `list` and `detail` actions for Groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer