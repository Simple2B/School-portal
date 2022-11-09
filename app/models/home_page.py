from core.models import ExtPage

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from modelcluster.fields import ParentalManyToManyField

from app.blocks.base_stream_block import BaseStreamBlock
from app.models.info_page import InfoPage


class HomePage(ExtPage):
    """Page with news and photos and additional settings."""

    def get_context(self, request):
        news = InfoPage.objects.filter(type="news")
        context = super().get_context(request)
        context["news"] = news
        return context

    gallery_images = ParentalManyToManyField(
        "app.ImagesGallaryPage",
        blank=True,
        related_name="home_page",
    )

    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page body",
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("gallery_images"),
        FieldPanel("body"),
    ]
