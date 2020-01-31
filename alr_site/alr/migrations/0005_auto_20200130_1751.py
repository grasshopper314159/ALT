# Generated by Django 2.2.7 on 2020-01-30 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alr', '0004_auto_20200130_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigaudio',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='comments',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='submission',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='audiotrim',
            name='last_listened_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='audiotrim',
            name='length',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='audiotrim',
            name='measurements',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='audiotrim',
            name='phonetic_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='audiotrim',
            name='score',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='audiotrim',
            name='word_count',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bigaudio',
            name='audio_trims',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='alr.AudioTrim'),
        ),
        migrations.AlterField(
            model_name='bigaudio',
            name='upload_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='assignments',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='alr.Assignment'),
        ),
        migrations.AlterField(
            model_name='class',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='alr.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='assignments',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='alr.Assignment'),
        ),
        migrations.AlterField(
            model_name='user',
            name='audio_trims',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='alr.AudioTrim'),
        ),
        migrations.AlterField(
            model_name='user',
            name='classes',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='alr.Class'),
        ),
        migrations.AlterField(
            model_name='user',
            name='languages',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='alr.Language'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='num_audio_files',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
