# Generated by Django 2.2.6 on 2020-04-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alr', '0002_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiotrim',
            name='last_listened_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
