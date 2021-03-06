from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='media' + '' + '/')

    def __str__(self):
        return self.image.name
