# Generated by Django 2.0.5 on 2018-06-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('europolapi', '0006_auto_20180529_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='HashedLicensePlate',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='licensePlate',
            field=models.TextField(blank=True, default='', max_length=64),
        ),
    ]
