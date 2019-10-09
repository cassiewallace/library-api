from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    """
    Custom permission to allow staff to see the list of users.
    """

    def has_permission(self, request, view):
        return request.user.is_staff


class IsStaffOrUser(permissions.BasePermission):
    """
    Custom permission to allow only staff or the user themselves
    to see a user's details.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user