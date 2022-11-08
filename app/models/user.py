from django.db import models
from django.contrib.auth.models import AbstractUser

# from app.blocks.base_stream_block import BaseStreamBlock
from app.models.school_class_page import SchoolClassPage


class User(AbstractUser):
    age = models.CharField(max_length=2)
    school_class = models.ForeignKey(
        SchoolClassPage, on_delete=models.SET_NULL, null=True
    )
    # TODO discover why do we need this object
    # BaseStreamBlock
