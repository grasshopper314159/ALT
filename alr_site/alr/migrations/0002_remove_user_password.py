# Generated by Django 2.2.7 on 2020-02-11 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
