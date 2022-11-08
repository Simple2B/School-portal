from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalKey

from app.models.profile import Profile
from app.models.school_class_page import SchoolClassPage
from app.models.schedule_page import SchedulePage


class LessonPage(Page):
    time = models.CharField(max_length=5)  # add validatin like "\d{2}:\d{2}"
    teacher = models.ForeignKey(
        Profile, null=True, on_delete=models.SET_NULL, related_name="lessons"
    )
    school_class = models.ForeignKey(
        SchoolClassPage,
        null=True,
        on_delete=models.SET_NULL,
        related_name="lessons",  # noqa: E501
    )
    schedule = ParentalKey(
        SchedulePage,
        null=True,
        on_delete=models.SET_NULL,
        related_name="lessons",  # noqa: E501
    )

    template = "app/lesson_page.html"

    content_panels = Page.content_panels + [
        FieldPanel("time"),
        FieldPanel("teacher"),
        FieldPanel("school_class"),
        FieldPanel("schedule"),
    ]
