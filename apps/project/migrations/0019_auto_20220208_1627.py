# Generated by Django 3.2.7 on 2022-02-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20220208_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='value_max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='value_min',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
