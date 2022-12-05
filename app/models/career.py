import uuid
from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class Career(Page):
    description = models.CharField(max_length=1000)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]
