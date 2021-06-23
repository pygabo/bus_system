# Generated by Django 3.1.12 on 2021-06-23 04:42

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusDriverModel',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('identification_number', models.CharField(max_length=150)),
                ('avatar', models.ImageField(upload_to='')),
                ('is_available', models.BooleanField()),
            ],
            options={
                'db_table': 'bus_driver',
            },
        ),
    ]
