# scans/views.py

from rest_framework import viewsets
from .models import ScanRequest
from .serializers import ScanRequestSerializer
from .tasks import start_scan_task

class ScanRequestViewSet(viewsets.ModelViewSet):
    queryset = ScanRequest.objects.all()
    serializer_class = ScanRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save(status='Pending')
        start_scan_task.delay(instance.id)
