# Generated by Django 4.0.7 on 2022-10-13 11:43

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_schoolclasspage_gallery_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolclasspage',
            name='gallery_images',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='school_class', to='app.imagesgallarypage'),
        ),
    ]
