# Generated by Django 2.0.5 on 2018-05-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('europolapi', '0004_auto_20180529_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='serialNumber',
            field=models.TextField(default='', max_length=128, primary_key=True),
        ),
    ]