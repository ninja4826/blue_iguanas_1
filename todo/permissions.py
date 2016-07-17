from rest_framework import permissions

class IsCreateOrListUsers(permissions.BasePermission):
    """
    Custom permission to only allow admins to get list of users
    """
    def has_permission(self, request, view):
        if request.method == 'POST' or view.action == 'me':
            return True
        
        return request.user.is_staff