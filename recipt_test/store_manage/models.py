from django.db import models
from recipt_test import settings

class Recipt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='own_user')
    reciptName = models.CharField(max_length=255)
    price = models.CharField(max_length=255, default='0')
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.reciptName
    
