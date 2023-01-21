# Generated by Django 4.1.4 on 2023-01-16 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0011_employee_is_hourly_alter_permission_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fitness.service'),
        ),
    ]