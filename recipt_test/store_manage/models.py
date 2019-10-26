from django.db import models
from recipt_test import settings

class Store(models.Model):
    clerk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clerk_store')
    storeName = models.CharField(max_length=255)
    
