from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Create Profile when a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(f"Signal fired: Profile created for user {instance.username}")

# Save profile when user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
