from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from app.models.school_class_page import SchoolClassPage


class Profile(Page):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    age = models.CharField(max_length=80, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name="+"
    )
    role_choices = [
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("super_user", "Super user"),
        ("admin", "Admin")
    ] 
    role = models.CharField(max_length=80, choices=role_choices)
    school_class = models.ForeignKey(SchoolClassPage, null=True, blank=True, on_delete=models.SET_NULL, related_name="member")

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("surname"),
        FieldPanel("age"),
        FieldPanel("image"),
        FieldPanel("role"),
        FieldPanel("school_class"),
    ]
