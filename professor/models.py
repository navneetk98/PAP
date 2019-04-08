from django.db import models


class Professor(models.Model):
    ID = models.SmallIntegerField(primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    area_of_interest = models.TextField(null=True)