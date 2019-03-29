from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpi = models.FloatField(blank=False, null=True)
    tier = models.IntegerField(blank=False, null=True)
    pending_join_requests = models.ManyToManyField("self", blank=True)
    group_id = models.IntegerField(null=True, blank=True)
    preference_of_professor = models.ManyToManyField("self", blank=True) #todo change this to professor list

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()