from rest_framework.permissions import BasePermission


class OwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object().owner:
            return True
        elif request.user.is_staff:
            return True
        return False

