from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.apps import apps

class Batch(models.Model):
    ID = models.SmallIntegerField(primary_key=True)
    batch_name = models.CharField(max_length=256)
    cutoff_cpi = models.FloatField(null=True, blank=True)
    group_size = models.SmallIntegerField()
#TODO    available_professor = models.ForeignKey(apps.get_model('professor', 'Professor'))


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(help_text="Department of the Admin",max_length=256)  #Mech admin should not be allowed to edit CSE data
#TODO    batches = models.ForeignKey(Batch)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Admin.objects.create(user=instance)
    instance.profile.save()
