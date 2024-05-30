from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135630ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135630", Testconnectors135630ViewSet, basename="testconnectors135630"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
