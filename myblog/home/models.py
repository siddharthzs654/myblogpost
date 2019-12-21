from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):

    title = models.CharField(max_length=100, blank=False, null=False)
    img = models.ImageField(upload_to="profilepics", height_field=None, width_field=None)
    content = models.TextField()
    tags = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete= models.SET_DEFAULT,default = "Anonymous")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"title: {self.title} author: {self.author}"