# Generated by Django 3.2.7 on 2022-01-04 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_register_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldchoice',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='project.field'),
        ),
    ]
