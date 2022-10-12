import black
from django.db import models

from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.fields import StreamField


from .blocks import BaseStreamBlock


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

    school_class = ParentalKey("SchoolClassPage", null=True, on_delete=models.SET_NULL, related_name="gallery_images")

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("collection"),
        FieldPanel("school_class")
    ]


class InfoPage(Page):
    """news, about_us, contacts"""

    choices = [
        ("news", "News"),
        ("about_us", "About_us"),
        ("contacts", "Contacts")
    ]

    type = models.CharField(choices=choices, max_length=20, default="news")

    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("type"),
    ]


class NewsItemsPage(Page):
    def get_context(self, request):
        news = InfoPage.objects.filter(type="news")
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
    school_class = models.ForeignKey(SchoolClassPage, null=True, blank=True, on_delete=models.SET_NULL, related_name="member")

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("surname"),
        FieldPanel("age"),
        FieldPanel("role"),
        FieldPanel("school_class"),
    ]


class SchedulePage(Page): pass
    # content_panels = Page.content_panels + [
    #     InlinePanel("lessons")
    # ]


class LessonPage(Page):
    time = models.CharField(max_length=5)   #add validatin like "\d{2}:\d{2}"
    teacher = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name="lessons")
    school_class = models.ForeignKey(SchoolClassPage, null=True, on_delete=models.SET_NULL, related_name="lessons")
    schedule = ParentalKey(SchedulePage, null=True, on_delete=models.SET_NULL, related_name="lessons")

    template = "app/lesson_page.html"

    content_panels = Page.content_panels + [
        FieldPanel("time"),
        FieldPanel("teacher"),
        FieldPanel("school_class"),
        FieldPanel("schedule")
    ]
