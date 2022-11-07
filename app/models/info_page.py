from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField


from app.blocks.base_stream_block import BaseStreamBlock
from app.models.profile import Profile


class InfoPage(Page):
    """news, about_us, contacts"""

    def get_context(self, request):
        teachers = Profile.objects.filter(role="teacher")
        context = super().get_context(request)
        context['teachers'] = teachers
        return context

    choices = [
        ("news", "News"),
        ("about_us", "About_us"),
        ("contacts", "Contacts")
    ]

    type = models.CharField(choices=choices, max_length=20, default="news")

    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("type"),
    ]
