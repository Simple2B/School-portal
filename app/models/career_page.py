from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from django.db import models

from app.blocks.base_stream_block import BaseStreamBlock


class CareerPage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["categories"] = [
            "Managment",
            "UX/UI",
            "Designer",
            "Software Development",
        ]
        context["careers"] = [
            "Career 1",
            "Career 2",
            "Career 3",
            "Career 4",
            "Career 5",
            "Career 6",
            "Career 7",
        ]
        return context

    question = models.CharField(max_length=255, default="")
    message = models.CharField(max_length=255, default="")
    phrase = models.CharField(max_length=255, default="")

    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page body",
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("question"),
        FieldPanel("message"),
        FieldPanel("phrase"),
        FieldPanel("body"),
    ]
