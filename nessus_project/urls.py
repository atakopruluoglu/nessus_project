# scans/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import ScanRequestViewSet

router = routers.DefaultRouter()
router.register(r'scans', ScanRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
