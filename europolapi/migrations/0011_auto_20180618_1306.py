# Generated by Django 2.0.5 on 2018-06-18 13:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('europolapi', '0010_auto_20180618_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='serialNumber',
            field=models.TextField(default=uuid.UUID('2a6f467d-5635-4b84-932f-e260e05b120b'), primary_key=True, serialize=False),
        ),
    ]
