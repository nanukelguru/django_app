from rest_framework import serializers
from .models import Articulo


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id', 'title', 'content', 'posted_on')
        read_only_field = ('posted_on', )