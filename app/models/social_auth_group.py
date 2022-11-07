from wagtail.contrib.modeladmin.options import ModelAdminGroup
from app.models.social_app_admin import SocialAppAdmin


class SocialAuthGroup(ModelAdminGroup):
    menu_label = 'Social Accounts'
    menu_icon = 'users'
    menu_order = 1200
    items = (SocialAppAdmin,)
