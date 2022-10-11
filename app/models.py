from email.policy import default
from pyexpat import model
from random import choices
from secrets import choice
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey


class ImagesGallaryPage(Page):
    image = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=True, 
            on_delete=models.SET_NULL, 
            related_name="+"
        )

    collection = models.ForeignKey(
        Collection, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name="+"
    )

    school_class = ParentalKey("SchoolClassPage", on_delete=models.CASCADE, related_name="gallery_images")

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("collection"),
        FieldPanel("school_class")
    ]


class InfoPage(Page):
    """news, about_us, contacts"""
    text = models.TextField()
    images = ParentalKey("ImagesGallaryPage", null=True, on_delete=models.SET_NULL, related_name="info_page")

    choices = [
        ("news", "News"),
        ("about_us", "About_us"),
        ("contacts", "Contacts")
    ]

    type = models.CharField(choices=choices, max_length=20, default="news")

    content_panels = Page.content_panels + [
        FieldPanel("images"),
        FieldPanel("text"),
        FieldPanel("type"),
    ]


class NewsItemsPage(Page):
    def get_context(self, request):
        news = InfoPage.objects.live().filter(type="news")
        context = super().get_context(request)
        context['news'] = news
        return context


class SchoolClassPage(Page): pass


class Profile(Page):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    age = models.CharField(max_length=80)
    
    role_choices = [
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("super_user", "Super user"),
        ("admin", "Admin")
    ] 
    role = models.CharField(max_length=80, choices=role_choices)
    school_class = models.ForeignKey(SchoolClassPage, null=True, on_delete=models.SET_NULL, related_name="member")

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("surname"),
        FieldPanel("age"),
        FieldPanel("role"),
        FieldPanel("school_class"),
    ]


class SchedulePage(Page): pass


class LessonPage(Page):
    time = models.CharField(max_length=5)   #add validatin like "\d{2}:\d{2}"
    teacher = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name="lessons")
    school_class = models.ForeignKey(SchoolClassPage, null=True, on_delete=models.SET_NULL, related_name="lessons")
    schedule = models.ForeignKey(SchedulePage, null=True, on_delete=models.SET_NULL, related_name="lessons")

    content_panels = Page.content_panels + [
        FieldPanel("time"),
        FieldPanel("teacher"),
        FieldPanel("school_class"),
        FieldPanel("schedule")
    ]
