# Generated by Django 2.2.28 on 2023-03-20 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourite',
            old_name='phone',
            new_name='phone_id',
        ),
    ]
