# Generated by Django 3.2.9 on 2021-12-06 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='Date_joined',
            new_name='date_joined',
        ),
    ]
