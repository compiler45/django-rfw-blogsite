from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read only permissions allowed for any request
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True

        # write permissions only allowed if logged in user is post author
        return obj.author == request.user

