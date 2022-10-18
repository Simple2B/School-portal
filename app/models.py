from random import choices
import black
from django.db import models
from django.contrib.auth.models import AbstractUser
from requests import request

from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
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

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("collection"),
    ]


class NewsItemsPage(Page):
    def get_context(self, request):
        news = InfoPage.objects.filter(type="news")
        context = super().get_context(request)
        context['news'] = news
        return context


class SchoolClassPage(Page):
    gallery_images = ParentalManyToManyField("ImagesGallaryPage", blank=True, related_name="school_class")

    content_panels = Page.content_panels + [
        FieldPanel("gallery_images")
    ]


class Profile(Page):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    age = models.CharField(max_length=80)
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


#-----------------------------------------------------PAGES-----------------------------------------------------


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


class HomePage(Page): 
    """Page with news and photos and additional settings."""

    def get_context(self, request):
        news = InfoPage.objects.filter(type="news")
        context = super().get_context(request)
        context['news'] = news
        return context

    gallery_images = ParentalManyToManyField("ImagesGallaryPage", blank=True, related_name="home_page")

    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    template = "app/test_home_page.html"

    content_panels = Page.content_panels + [
        FieldPanel("gallery_images"),
        FieldPanel("body")
    ]


class ProfilePage(Page):
    def get_context(self, request):
        profile = Profile.objects.get(pk=request.user.pk)
        context = super().get_context(request)
        context['profile'] = profile
        return context
    
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]


class ListPage(Page):
    """
        Class that contains list of objects of Root directory.
        Not sure about this class.
    """
    pass


#-----------------------------------------------------CUSTOM USER MODEL-----------------------------------------------------


class User(AbstractUser):
    age = models.CharField(max_length=2)
    school_class = models.ForeignKey(SchoolClassPage, on_delete=models.SET_NULL, null=True)

    # def save(self, *args, **kwargs):
    #     Profile.objects.create(name=kwargs['First name'], surname=kwargs['last_name'], age=kwargs['age'], role_choices='Student', school_class=kwargs['school_class'])
    #     super().save(*args, **kwargs)
    
# School-portal/home/templates/home/welcome_page.html