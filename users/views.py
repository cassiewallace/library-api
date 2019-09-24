from django.contrib.auth.models import User, Group
from users.serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides `list` and `detail` actions for Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides `list` and `detail` actions for Groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer