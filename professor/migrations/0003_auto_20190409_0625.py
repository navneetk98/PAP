# Generated by Django 2.1.7 on 2019-04-09 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_professor_max_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
