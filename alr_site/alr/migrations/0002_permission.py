# Generated by Django 3.0.2 on 2020-04-07 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_audio_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alr.BigAudio')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alr.User')),
            ],
            options={
                'unique_together': {('big_audio_id', 'user_id')},
            },
        ),
    ]
