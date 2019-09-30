from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')  #media폴더안에 존재하는 images폴더를 가리킴.

    def __str__(self):
        return self.title
