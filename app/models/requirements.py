from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from app.models import Career


class Requirement(Page):
    career_object = models.ForeignKey(Career, on_delete=models.PROTECT)

    content_panels = Page.content_panels + [FieldPanel("career_object")]
