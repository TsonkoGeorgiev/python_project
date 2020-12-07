from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    email = models.EmailField(blank=False)
    profile_photo = models.ImageField(upload_to='profiles')
    tel_number = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
