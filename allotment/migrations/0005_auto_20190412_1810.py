# Generated by Django 2.1.7 on 2019-04-12 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allotment', '0004_auto_20190408_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
