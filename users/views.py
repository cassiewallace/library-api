from django.contrib.auth.models import User, Group

from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.permissions import IsStaff, IsStaffOrUser
from users.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Provides `list`, `create`, `retrieve`, `update`, and `destroy` 
    actions for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsStaffOrUser]
        else:
            self.permission_classes = [IsStaff]
        return super(self.__class__, self).get_permissions()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides `list` and `detail` actions for Groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer