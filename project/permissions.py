from rest_framework import permissions


class IsAuthenticatedOrReadOnlyAndOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Permitir métodos GET, HEAD, OPTIONS (lectura)
        return request.user.is_authenticated  # Solo usuarios autenticados pueden realizar otras acciones

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user  # Solo el autor del artículo puede editarlo