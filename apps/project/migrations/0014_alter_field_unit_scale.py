# Generated by Django 3.2.7 on 2022-01-05 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20220104_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='unit_scale',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10),
        ),
    ]