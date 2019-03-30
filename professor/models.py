from django.db import models

#from administrator.models import Batch
#from django.apps import apps

class Professor(models.Model):
    ID = models.SmallIntegerField(primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    area_of_interest = models.TextField(null=True)
#TODO    batch = models.ForeignKey(apps.get_model('administrator', 'Batch'))