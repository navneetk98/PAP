# Generated by Django 2.1.7 on 2019-04-08 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_remove_profile_preference_of_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tier',
        ),
        migrations.AddField(
            model_name='profile',
            name='group_ID',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
