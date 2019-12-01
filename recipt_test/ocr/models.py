from django.db import models
from recipt_test import settings

class Recipt_img(models.Model):
    ownuser = models.ForeignKey(settings.AUTH_USER_MODEL, default=None , on_delete=models.CASCADE, related_name='recipt_img_user')
    recipt_img_url = models.ImageField(upload_to="recipt_img")