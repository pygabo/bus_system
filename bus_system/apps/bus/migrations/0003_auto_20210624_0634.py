# Generated by Django 3.1.12 on 2021-06-24 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus_driver', '0002_auto_20210623_0522'),
        ('bus', '0002_auto_20210624_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busmodel',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bus_driver.busdrivermodel'),
        ),
    ]
