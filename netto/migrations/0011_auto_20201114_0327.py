# Generated by Django 3.1.2 on 2020-11-14 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netto', '0010_auto_20201114_0318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='commanline',
            new_name='commandline',
        ),
    ]