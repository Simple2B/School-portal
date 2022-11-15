import datetime
from django.test import Client
from wagtail.models import Page, Site
from wagtail.tests.utils import WagtailPageTestCase, WagtailPageTests

from app.models import (
    FormPage,
    HomePage,
    ImagesGallaryPage,
    InfoPage,
    LessonPage,
    Profile,
    ProfilePage,
    SchedulePage,
    SchoolClassPage,
)


class TestPageExists(WagtailPageTestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.parent_page = Page.get_first_root_node()
        cls.schedule = SchedulePage(title="Set up schedule", slug="set_up_schedule")
        cls.parent_page.add_child(instance=cls.schedule)
        cls.teacher = Profile(
            title="Ivan Petrov",
            slug="teacher",
            name="Ivan",
            surname="Petrov",
            role="teacher",
        )
        cls.parent_page.add_child(instance=cls.teacher)
        cls.school_class = SchoolClassPage(
            title="Set up school class", slug="set_up_school_class"
        )
        cls.parent_page.add_child(instance=cls.school_class)
        cls.teacher.save()

    def test_home_page_exists(self):
        page = HomePage(title="Home page", slug="core", path="/blog/", pk=1, depth=1)
        home = self.parent_page.get_children()[0]
        home.add_child(instance=page)
        page = home.get_children()[0]
        self.assertEqual(page.title, "Home page")
        self.assertPageIsRoutable(page)

    def test_info_page_exists(self):
        page = InfoPage(title="Info page", slug="info_page")
        home = self.parent_page.get_children()[0]
        home.add_child(instance=page)
        page = home.get_children()[0]
        self.assertEqual(page.title, "Info page")
        self.assertPageIsRoutable(page)

    def test_form_page_exists(self):
        page = FormPage(title="Form page", slug="form_page")
        home = self.parent_page.get_children()[0]
        home.add_child(instance=page)
        page = home.get_children()[0]
        self.assertEqual(page.title, "Form page")
        self.assertPageIsRoutable(page)

    def test_images_gallary_page_exists(self):
        page = ImagesGallaryPage(
            title="Images gallary page", slug="images_gallary_page"
        )
        home = self.parent_page.get_children()[0]
        home.add_child(instance=page)
        page = home.get_children()[0]
        self.assertEqual(page.title, "Images gallary page")
        self.assertPageIsRoutable(page)

    def test_lesson_page_exists(self):
        page = LessonPage(
            title="Lesson page",
            slug="lesson_page",
            time="12:45",
            teacher=self.teacher,
            schedule=self.schedule,
            school_class=self.school_class,
        )
        home = self.parent_page.get_children()[0]
        home.add_child(instance=page)
        page = home.get_children()[0]
        self.assertEqual(page.title, "Lesson page")
        self.assertPageIsRoutable(page)

    def test_profile_page_exists(self):
        page = ProfilePage(title="Profile page", slug="profile_page")
        home = self.parent_page.get_children()[0]
        home.add_child(instance=page)
        page = home.get_children()[0]
        self.assertEqual(page.title, "Profile page")
        self.assertPageIsRoutable(page)

    def test_schedule_page_exists(self):
        page = SchedulePage(title="Schedule page", slug="schedule_page")
        home = self.parent_page.get_children()[0]
        home.add_child(instance=page)
        page = home.get_children()[0]
        self.assertEqual(page.title, "Schedule page")
        self.assertPageIsRoutable(page)

    def test_school_class_page_exists(self):
        page = SchoolClassPage(title="School class page", slug="school_class_page")
        home = self.parent_page.get_children()[0]
        home.add_child(instance=page)
        page = home.get_children()[0]
        self.assertEqual(page.title, "School class page")
        self.assertPageIsRoutable(page)

    def test_profile_exists(self):
        page = Profile(
            title="Profile",
            slug="profile",
            name="Jack",
            surname="Shcherbyna",
            role="student",
        )
        home = self.parent_page.get_children()[0]
        home.add_child(instance=page)
        page = home.get_children()[0]
        self.assertEqual(page.title, "Profile")
        self.assertPageIsRoutable(page)
