from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image



class Profile(models.Model):

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepics/default.jpg',upload_to='profilepics',blank=True)
    status = models.CharField(max_length=30)
    about = models.TextField()

    def save(self,*args, **kwargs):
        super(Profile,self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



