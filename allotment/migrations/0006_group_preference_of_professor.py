# Generated by Django 2.1.7 on 2019-04-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allotment', '0005_auto_20190412_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='preference_of_professor',
            field=models.CharField(max_length=256, null=True),
        ),
    ]