from rest_framework import permissions

from user.models import User


class IsOwnerSelectionStuff(permissions.BasePermission):
    message = "У Вас нет прав редактировать подборки"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.role in [User.MODERATOR, User.ADMIN]:
            return True
        return False


class IsOwnerAdStuff(permissions.BasePermission):
    message = "У Вас нет прав редактировать объявления"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [User.MODERATOR, User.ADMIN]:
            return True
        return False
