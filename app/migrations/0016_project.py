# Generated by Django 4.1.3 on 2022-12-02 08:37

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
        ("wagtailimages", "0024_index_image_file_hash"),
        ("app", "0015_projectspage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(default="", max_length=255)),
                ("category", models.CharField(default="", max_length=255)),
                ("description", models.CharField(default="", max_length=255)),
                ("info", models.TextField()),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading_text",
                                            wagtail.blocks.CharBlock(
                                                form_classname="title", required=True
                                            ),
                                        ),
                                        (
                                            "size",
                                            wagtail.blocks.ChoiceBlock(
                                                blank=True,
                                                choices=[
                                                    ("", "Select a header size"),
                                                    ("h2", "H2"),
                                                    ("h3", "H3"),
                                                    ("h4", "H4"),
                                                ],
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "paragraph_block",
                                wagtail.blocks.RichTextBlock(
                                    template="blocks/paragraph_block.html"
                                ),
                            ),
                            (
                                "image_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "caption",
                                            wagtail.blocks.CharBlock(required=False),
                                        ),
                                        (
                                            "attribution",
                                            wagtail.blocks.CharBlock(required=False),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "embed_block",
                                wagtail.embeds.blocks.EmbedBlock(
                                    max_height=338,
                                    max_width=600,
                                    template="blocks/embed_block.html",
                                ),
                            ),
                            (
                                "item_block",
                                wagtail.blocks.StructBlock(
                                    [("heading_text", wagtail.blocks.CharBlock())]
                                ),
                            ),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Page body",
                    ),
                ),
                (
                    "project_picture",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]