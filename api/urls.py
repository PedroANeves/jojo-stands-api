from django.urls import path, include
from rest_framework import routers

from . import views


class CodicesRouter(routers.DefaultRouter):
    APIRootView = views.CodicesApisView()


router = CodicesRouter()
router.register(r'jojo', views.StandViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',
        include('rest_framework.urls',
        namespace='rest_framework')),
]