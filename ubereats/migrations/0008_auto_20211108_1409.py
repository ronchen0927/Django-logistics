# Generated by Django 3.2.9 on 2021-11-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubereats', '0007_auto_20211106_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_driver_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_store_completed',
            field=models.BooleanField(default=False),
        ),
    ]
