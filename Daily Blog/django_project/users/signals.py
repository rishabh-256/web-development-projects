from django.db.models.signals import post_save

# this is a signal which gets fired after an object is saved
from django.contrib.auth.models import User

# the user model here is the sender. Since its gonnna send the signal
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
