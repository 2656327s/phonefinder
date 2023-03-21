# Generated by Django 2.2.28 on 2023-03-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20230320_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('brand', models.CharField(max_length=128)),
                ('releaseYear', models.IntegerField(max_length=4)),
                ('storage', models.IntegerField(max_length=10)),
                ('resolution', models.CharField(max_length=32)),
                ('ram', models.IntegerField(max_length=32)),
                ('picture', models.CharField(max_length=512)),
                ('isFavourite', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'phones',
            },
        ),
    ]
