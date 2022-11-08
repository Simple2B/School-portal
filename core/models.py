from wagtail.models import Page
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from wagtailmetadata.models import MetadataPageMixin

from django.db import models
from django.utils.translation import gettext_lazy as _


class ExtPage(MetadataPageMixin, Page):
    keywords = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=("meta keywords"),
    )

    search_fields = Page.search_fields + [
        index.SearchField("keywords", patrial_match=True, boost=2)
    ]

    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel("slug"),
                FieldPanel("seo_title", heading=_("Title tag")),
                FieldPanel("search_description"),
                FieldPanel("keywords"),
                FieldPanel("search_image"),
            ],
            heading=_("For search engines"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("show_in_menus"),
            ],
            heading=_("For site menus"),
        ),
    ]

    settings_panels = Page.settings_panels

    class Meta:
        abstract = True
