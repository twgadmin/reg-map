# Generated by Django 3.2.7 on 2022-01-04 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0008_alter_register_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('range_upper', models.PositiveIntegerField()),
                ('range_lower', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('MUX', 'Multiplex'), ('INT', 'Signed Integer'), ('UINT', 'Unsigned Integer'), ('ASCII', 'Text'), ('RES', 'Reserved'), ('FLAG_AH', 'Flag, Active High'), ('FLAG_AL', 'Flag, Active Low'), ('DOUBLE', 'Double Floating Point')], default='RES', max_length=10)),
                ('unit_scale', models.DecimalField(decimal_places=5, max_digits=10)),
                ('unit_type', models.CharField(blank=True, max_length=4)),
                ('name', models.CharField(blank=True, default='', max_length=10)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_field', to=settings.AUTH_USER_MODEL)),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='project.register')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_field', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
    ]
