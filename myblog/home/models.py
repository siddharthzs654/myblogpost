from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Articles(models.Model):

    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.SET_DEFAULT,default = "Anonymous")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title