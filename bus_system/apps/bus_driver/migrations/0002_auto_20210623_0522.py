# Generated by Django 3.1.12 on 2021-06-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdrivermodel',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
