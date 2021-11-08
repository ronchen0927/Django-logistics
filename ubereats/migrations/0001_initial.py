# Generated by Django 3.2.9 on 2021-11-05 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='司機名稱')),
            ],
            options={
                'db_table': 'tb_driver',
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('food', models.CharField(max_length=30, verbose_name='食物名稱')),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ubereats.driver')),
            ],
            options={
                'db_table': 'tb_order',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='店家名稱')),
                ('food', models.CharField(max_length=30, verbose_name='食物名稱')),
            ],
            options={
                'db_table': 'tb_store',
                'unique_together': {('name', 'food')},
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platform', to='ubereats.driver')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platform', to='ubereats.order')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platform', to='ubereats.store')),
            ],
            options={
                'db_table': 'tb_platform',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ubereats.store'),
        ),
    ]