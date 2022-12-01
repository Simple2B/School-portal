from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from django.db import models

from app.blocks.base_stream_block import BaseStreamBlock


class ProjectsPage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["projects"] = [
            {
                "name": "FastAPI Project",
                "categorie": "medical",
                "description": "The Best FastAPI Project",
                "info": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum distinctio nemo harum doloribus. Accusantium mollitia sapiente, quis alias rem aperiam. Unde dicta deleniti, explicabo eum aut nobis voluptates ex asperiores.",
                "project_picture": "projects/project_01.png",
            },
            {
                "name": "JS Project",
                "categorie": "mobility",
                "description": "The Best FastAPI Project",
                "info": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum distinctio nemo harum doloribus. Accusantium mollitia sapiente, quis alias rem aperiam. Unde dicta deleniti, explicabo eum aut nobis voluptates ex asperiores.",
                "project_picture": "projects/project_01.png",
            },
            {
                "name": "Django Project",
                "categorie": "ifrastructure",
                "description": "The Best FastAPI Project",
                "info": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum distinctio nemo harum doloribus. Accusantium mollitia sapiente, quis alias rem aperiam. Unde dicta deleniti, explicabo eum aut nobis voluptates ex asperiores.",
                "project_picture": "projects/project_01.png",
            },
            {
                "name": "ML Project",
                "categorie": "cultural",
                "description": "The Best FastAPI Project",
                "info": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum distinctio nemo harum doloribus. Accusantium mollitia sapiente, quis alias rem aperiam. Unde dicta deleniti, explicabo eum aut nobis voluptates ex asperiores.",
                "project_picture": "projects/project_01.png",
            },
        ]
        return context

    question = models.CharField(max_length=255, default="")
    message = models.CharField(max_length=255, default="")
    phrase = models.CharField(max_length=255, default="")

    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page body",
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("question"),
        FieldPanel("message"),
        FieldPanel("phrase"),
        FieldPanel("body"),
    ]
