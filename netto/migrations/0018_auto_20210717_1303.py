# Generated by Django 3.1.4 on 2021-07-17 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netto', '0017_auto_20210717_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='location',
        ),
        migrations.RemoveField(
            model_name='device',
            name='position',
        ),
    ]
