from django.db import models
from django.contrib.auth.models import User
from administrator.models import Batch
from professor.models import Professor


class Group(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    group_id = models.SmallIntegerField(primary_key=True)
    mentor = models.ForeignKey(Professor, models.SET_NULL, null=models.SET_NULL)
