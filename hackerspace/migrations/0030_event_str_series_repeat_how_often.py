# Generated by Django 2.2.6 on 2019-11-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0029_auto_20191126_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='str_series_repeat_how_often',
            field=models.CharField(blank=True, choices=[('weekly', 'weekly'), ('biweekly', 'biweekly'), ('monthly', 'monthly')], max_length=50, null=True, verbose_name='Series How often repeating?'),
        ),
    ]
