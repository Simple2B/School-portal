# Generated by Django 4.1.3 on 2022-12-01 12:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
        ("app", "0012_career_requirement_advantage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Candiadate",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_phone_number",
                                message="Input correcr phone number",
                                regex="\\d{10}",
                            )
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("cv", models.TextField()),
                ("proposal", models.TextField()),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
