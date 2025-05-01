from rest_framework import permissions

class IsAdminOrAssignedUser(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        # Admins have full access
        if request.user.role == 'admin':
            return True

        # Regular users: only if task is assigned to them
        if request.method in permissions.SAFE_METHODS or request.method in ['PUT', 'PATCH']:
            return obj.assigned_to == request.user

        return False  
