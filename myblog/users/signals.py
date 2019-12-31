from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("profile****************************")
    if created:
        print("created profile***************************")
        user_profile = Profile.objects.create(username=instance)


@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    print("saved profile****************************8")
    instance.profile.save()

