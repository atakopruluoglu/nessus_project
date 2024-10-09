from django.db import models

class ScanRequest(models.Model):
    ip_list = models.TextField()  # IP listesi, virgülle ayrılmış
    status = models.CharField(max_length=20, default='Pending')  # 'Pending', 'Running', 'Completed'
    result = models.TextField(blank=True, null=True)  # Tarama sonuçları

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scan {self.id} - {self.status}"
