from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalManyToManyField


class SchoolClassPage(Page):
    gallery_images = ParentalManyToManyField(
        "app.ImagesGallaryPage", blank=True, related_name="school_class"
    )

    content_panels = Page.content_panels + [FieldPanel("gallery_images")]
