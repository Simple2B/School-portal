from django.db import models
from django.core.validators import RegexValidator
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from app.models import Career


class Candiadate(Page):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r"\d{3}-\d{3}-\d{2}-\d{2}",
                message="Input correcr phone number XXX-XXX-XX-XX",
                code="invalid_phone_number",
            )
        ],
    )
    email = models.EmailField()

    cv_file = models.BinaryField(editable=True, default=bytes("default value", "utf-8"))
    cv_file_name = models.CharField(max_length=255, default="default cv file name")

    proposal = models.TextField()
    career_object = models.ForeignKey(Career, on_delete=models.PROTECT, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("full_name"),
        FieldPanel("phone_number"),
        FieldPanel("email"),
        FieldPanel("cv_file"),
        FieldPanel("cv_file_name"),
        FieldPanel("proposal"),
        FieldPanel("career_object"),
    ]
