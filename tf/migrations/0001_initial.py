# Generated by Django 2.1.7 on 2019-04-08 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('allotment', '0004_auto_20190408_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamFormation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_no', models.IntegerField(null=True)),
                ('requests', models.CharField(max_length=256, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.fields.CharField, to='allotment.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
