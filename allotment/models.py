from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class GroupInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_group_leader = models.BooleanField(default=False)
#TODO    preference_of_professeor = models.OneTOManyRel(Professor)
    group_id = models.SmallIntegerField(null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        GroupInfo.objects.create(user=instance)
    instance.profile.save()

