from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import routers

from .models import Stand
from .serializers import StandSerializer


class CodicesApisView(routers.APIRootView):
    """APIs avaliable at https://api.codices.one"""


class StandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer

