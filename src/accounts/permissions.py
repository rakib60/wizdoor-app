from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, userobj):
        if request.user:
            return userobj == request.user
        return False