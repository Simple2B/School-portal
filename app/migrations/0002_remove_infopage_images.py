# Generated by Django 4.0.7 on 2022-10-12 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infopage',
            name='images',
        ),
    ]
