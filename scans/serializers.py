
from rest_framework import serializers
from .models import ScanRequest

class ScanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanRequest
        fields = '__all__'
