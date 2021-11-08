# Generated by Django 3.2.9 on 2021-11-05 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubereats', '0004_auto_20211105_1124'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='driver',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='store',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='store',
            name='drink',
        ),
        migrations.RemoveField(
            model_name='store',
            name='food',
        ),
    ]