# Generated by Django 4.1.4 on 2022-12-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='mail',
            field=models.EmailField(default='email1@mail.ru', max_length=254),
        ),
        migrations.AddField(
            model_name='employee',
            name='mail',
            field=models.EmailField(default='email@mail.ru', max_length=254),
        ),
    ]
