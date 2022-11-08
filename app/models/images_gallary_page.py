from django.db import models
from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel


class ImagesGallaryPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    collection = models.ForeignKey(
        Collection,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("collection"),
    ]
