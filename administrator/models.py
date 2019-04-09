from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from professor.models import Professor
from .choice import DEPARTMENT_CHOICES


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.SmallIntegerField(choices=DEPARTMENT_CHOICES, null=True)


class Batch(models.Model):
    ID = models.SmallIntegerField(primary_key=True)
    batch_name = models.CharField(max_length=256)
    cutoff_cpi = models.FloatField(null=True, blank=True)
    group_size = models.SmallIntegerField()
    is_team_formation_allowed = models.BooleanField(default=False)
    is_preference_filling_allowed = models.BooleanField(default=False)
    professor = models.ManyToManyField(Professor)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)


@receiver(post_save, sender=User)
def update_user_admin(sender, instance, created, **kwargs):
    if created and (User.is_staff == True):
        Admin.objects.create(user=instance)
        instance.admin.save()
        #admin.save()
