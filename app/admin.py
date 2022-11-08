from django.contrib import admin
from wagtail.contrib.modeladmin.options import modeladmin_register

from app.models.user import User
from app.models.social_auth_group import SocialAuthGroup


admin.site.register(User)
modeladmin_register(SocialAuthGroup)
