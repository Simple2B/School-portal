from django import template
from app.utils import get_menu


register = template.Library()


@register.inclusion_tag("tags/header.html", takes_context=True)
def get_header(context):
    return {
        "request": context["request"],
        "header_menu": get_menu(context),
    }


@register.inclusion_tag("tags/footer.html", takes_context=True)
def get_footer(context):
    return {
        "request": context["request"],
        "footer_menu": get_menu(context),
    }
