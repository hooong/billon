from django.db import models
from recipt_test import settings

# 영수증 이미지 모델
class Recipt_img(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipt_img')
    recipt_img_url = models.ImageField(upload_to="recipt_img")
