from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.core.blocks import RichTextBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.panels import FieldPanel


class SupportHomePage(Page):
    heading = RichTextField(
        null=False,
        blank=False,
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("banner_image"),
    ]


class SupportPage(Page):
    heading = RichTextField(
        null=False,
        blank=False,
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    overview_text = StreamField(
        [
            ("heading", CharBlock()),
            ("paragraph", RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("video", EmbedBlock()),
        ],
        block_counts={
            "heading": {"min_num": 1},
            "image": {"max_num": 5},
            "video": {"max_num": 5},
        },
        use_json_field=True,
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("banner_image"),
        FieldPanel("overview_text"),
    ]