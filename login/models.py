from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from professor.models import Professor
from administrator.models import Batch


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpi = models.FloatField(blank=False, null=True)
    #group_ID = models.SmallIntegerField(null=True, blank=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created and (instance.is_staff != True):
        Profile.objects.create(user=instance)
        instance.profile.save()


# def remove_user(sender, instance, **kwargs):
#    user = instance.user_id
#    User.objects.filter(id=user).delete()
#
# pre_delete.connect(remove_user, sender=Profile)