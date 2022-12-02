from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from django.db import models
from .user import User

from app.blocks.base_stream_block import BaseStreamBlock


class Project(Page):
    def get_context(self, request):
        context = super().get_context(request)
        return context

    name = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=255, default="")
    description = models.CharField(max_length=255, default="")
    info = models.TextField()
    project_picture = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page body",
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("category"),
        FieldPanel("description"),
        FieldPanel("info"),
        FieldPanel("project_picture"),
    ]
