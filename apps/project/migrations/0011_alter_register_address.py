# Generated by Django 3.2.7 on 2022-01-04 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_fieldchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.PositiveIntegerField(),
        ),
    ]
