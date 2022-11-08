from wagtail.contrib.modeladmin.options import ModelAdmin
from allauth.socialaccount.models import SocialApp


class SocialAppAdmin(ModelAdmin):
    model = SocialApp
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exlude_from_explorer = False
    list_display = ["name", "provider"]
