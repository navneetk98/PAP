# Generated by Django 2.1.7 on 2019-04-12 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_profile_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='group_ID',
        ),
    ]
