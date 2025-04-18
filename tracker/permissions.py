from rest_framework.permissions import BasePermission


class IsHabitOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.pk == obj.pk
