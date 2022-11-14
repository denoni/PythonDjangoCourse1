from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to update theis own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    

class UpdateOwnStatus(permissions.BasePermission):
    """Allows users to update their own status"""
    
    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id