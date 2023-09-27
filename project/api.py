from .models import Articulo
from rest_framework import viewsets, permissions
from .serializers import ArticuloSerializer


class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = ArticuloSerializer