# Generated by Django 3.2 on 2021-04-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('istanbulnufus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='istanbulnufus',
            name='givenWater',
            field=models.FloatField(default=-1),
        ),
    ]
