from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only staff to create and edit books.
    """

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in permissions.SAFE_METHODS
