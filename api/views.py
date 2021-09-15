from django.shortcuts import render
from rest_framework import viewsets

from .models import Stand
from .serializers import StandSerializer


class StandViewSet(viewsets.ModelViewSet):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer

