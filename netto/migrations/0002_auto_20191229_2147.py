# Generated by Django 3.0 on 2019-12-29 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='ip_add',
            new_name='ip_address',
        ),
    ]