from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать или удалять только свои привычки.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешено для чтения для всех запросов если они помечены как публичные.
        if request.method in permissions.SAFE_METHODS and obj.is_public is True:
            return True

        # Разрешено для записи только владельцу привычки.
        return obj.user == request.user
