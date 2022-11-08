from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalManyToManyField

from app.models.images_gallary_page import ImagesGallaryPage  # noqa: F401


class SchoolClassPage(Page):
    gallery_images = ParentalManyToManyField(
        "ImagesGallaryPage", blank=True, related_name="school_class"
    )

    content_panels = Page.content_panels + [FieldPanel("gallery_images")]
