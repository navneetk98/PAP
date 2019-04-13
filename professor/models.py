from django.db import models


class Professor(models.Model):
    ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    max_group = models.SmallIntegerField(default=1)
    area_of_interest = models.TextField(null=True)
