# Generated by Django 2.2.6 on 2019-11-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0030_event_str_series_repeat_how_often'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='float_lat',
            field=models.FloatField(blank=True, null=True, verbose_name='Lat'),
        ),
        migrations.AddField(
            model_name='event',
            name='float_lon',
            field=models.FloatField(blank=True, null=True, verbose_name='Lon'),
        ),
    ]
