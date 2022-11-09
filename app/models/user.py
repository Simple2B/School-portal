from django.db import models
from django.contrib.auth.models import AbstractUser

from app.models.school_class_page import SchoolClassPage


class User(AbstractUser):
    age = models.CharField(max_length=2)
    school_class = models.ForeignKey(
        SchoolClassPage, on_delete=models.SET_NULL, null=True
    )
