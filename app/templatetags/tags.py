from django import template
from app.utils import get_menu
from app.models import Profile
from django.utils.functional import SimpleLazyObject


register = template.Library()


@register.inclusion_tag("tags/header.html", takes_context=True)
def get_header(context):
    responce = {
        "request": context["request"],
        "header_menu": get_menu(context),
        "user": context["request"].user,
    }
    if not context["request"].user.is_anonymous:
        responce["profile"] = Profile.objects.get(email=context["request"].user.email)

    return responce


@register.inclusion_tag("tags/footer.html", takes_context=True)
def get_footer(context):
    return {
        "request": context["request"],
        "footer_menu": get_menu(context),
    }
