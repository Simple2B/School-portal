from django import template
from app.utils import get_menu
from app.models import Profile
from django.utils.functional import SimpleLazyObject
from django.conf import settings


register = template.Library()


@register.inclusion_tag("tags/header.html", takes_context=True)
def get_header(context):
    contact_us, header_menu = get_menu(context)
    response = {
        "request": context["request"],
        "header_menu": header_menu,
        "user": context["request"].user,
        "contact_us": contact_us,
        "MEDIA_URL": settings.MEDIA_URL,
    }
    if (
        not context["request"].user.is_anonymous
        and not context["request"].user.is_superuser
    ):
        response["profile"] = Profile.objects.get(email=context["request"].user.email)

    return response


@register.inclusion_tag("tags/footer.html", takes_context=True)
def get_footer(context):
    contact_us, footer_menu = get_menu(context)

    return {
        "request": context["request"],
        "footer_menu": footer_menu,
        "contact_us": contact_us,
    }


@register.inclusion_tag("tags/language_button.html", takes_context=True)
def language_button(context):
    return {"request": context["request"], "page": context["page"]}
