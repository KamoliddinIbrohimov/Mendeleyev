from django.shortcuts import render
from rest_framework import viewsets

from elements import models
from .serializers import ElementSerializer


# Create your views here.


class ElementsViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer
    queryset = models.Element.objects.all()
