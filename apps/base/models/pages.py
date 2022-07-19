from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.core.blocks import RichTextBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import (
    FieldPanel,
)


class HomePage(Page):
    body = StreamField(
        [
            ("heading", CharBlock(label=_("Heading"))),
            ("paragraph", RichTextBlock(label=_("Paragraph"))),
            ("image", ImageChooserBlock(label=_("Image"))),
            ("video", EmbedBlock(label=_("Video"))),
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
    content_panels = Page.content_panels + [FieldPanel("body")]


class StandardPage(Page):
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField(
        [
            ("heading", CharBlock(label=_("Heading"))),
            ("paragraph", RichTextBlock(label=_("Paragraph"))),
            ("image", ImageChooserBlock(label=_("Image"))),
            ("video", EmbedBlock(label=_("Video"))),
        ],
        use_json_field=True,
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("banner_image"),
        FieldPanel("body"),
    ]
