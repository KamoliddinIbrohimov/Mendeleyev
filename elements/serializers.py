from rest_framework import serializers
from .models import Element


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ('id', 'number', 'name', 'symbol', 'extract', 'source', 'category', 'atomic_weight', 'colors')
