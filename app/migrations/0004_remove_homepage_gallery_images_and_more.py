# Generated by Django 4.0.7 on 2022-10-13 11:58

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_schoolclasspage_gallery_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='gallery_images',
        ),
        migrations.AddField(
            model_name='homepage',
            name='gallery_images',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='home_page', to='app.imagesgallarypage'),
        ),
    ]
