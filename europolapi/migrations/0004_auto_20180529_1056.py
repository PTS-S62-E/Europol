# Generated by Django 2.0.5 on 2018-05-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('europolapi', '0003_auto_20180529_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='id',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='HashedLicensePlate',
            field=models.TextField(default='', max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='originCountry',
            field=models.TextField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='serialNumber',
            field=models.TextField(default='', max_length=128),
        ),
    ]
