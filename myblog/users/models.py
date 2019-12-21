from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profilepics')
    status = models.CharField(max_length=30)
    about = models.TextField()
