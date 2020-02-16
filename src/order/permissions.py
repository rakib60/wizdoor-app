from rest_framework import permissions


class IsCustomerOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return str(obj.customer) == str(request.user.username)