from email.policy import default
from pyexpat import model
from secrets import choice
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalKey


class ImagesGallaryPage(Page):
    image = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=True, 
            on_delete=models.SET_NULL, 
            related_name="+"
        )

    collection = models.ForeignKey(
        Collection, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("collection"),
    ]


class InfoPage(Page):
    """news, about_us, contacts"""
    text = models.TextField()
    images = ParentalKey("ImagesGallaryPage", null=True, on_delete=models.SET_NULL, related_name="info_page")

    choices = [
        ("news", "news"),
        ("about_us", "about_us"),
        ("contacts", "contacts")
    ]

    type = models.CharField(choices=choices, max_length=20, default="news")

    content_panels = Page.content_panels + [
        FieldPanel("images"),
        FieldPanel("text"),
        FieldPanel("type"),
    ]


# class NewsItemsPage(Page):
#     def get_context(self, request, *args, **kwargs):
#         context = super().get_context(request, *args, **kwargs)
