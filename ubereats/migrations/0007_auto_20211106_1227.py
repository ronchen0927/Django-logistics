# Generated by Django 3.2.9 on 2021-11-06 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubereats', '0006_auto_20211106_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ubereats.driver'),
        ),
        migrations.AlterField(
            model_name='order',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ubereats.store'),
        ),
    ]
