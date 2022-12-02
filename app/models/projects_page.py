from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from django.db import models
from django.conf import settings
from .user import User
from .project import Project

from app.blocks.base_stream_block import BaseStreamBlock


class ProjectsPage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["projects"] = Project.objects.all()
        context["MEDIA_URL"] = settings.MEDIA_URL
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
