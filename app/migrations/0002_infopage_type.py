# Generated by Django 4.0.7 on 2022-10-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopage',
            name='type',
            field=models.CharField(choices=[('news', 'news'), ('about_us', 'about_us'), ('contacts', 'contacts')], default='news', max_length=20),
        ),
    ]
