from django import template
from wagtail.models import Site


register = template.Library()


def get_menu(context):
    """Function for header and footer. Returns menu items"""

    menu = [Site.find_for_request(context["request"]).root_page]
    [
        menu.append(item)
        for item in Site.find_for_request(context["request"])
        .root_page.get_children()
        .live()
        .in_menu()
    ]

    return menu


@register.inclusion_tag("tags/header.html", takes_context=True)
def get_header(context):
    return {
        "request": context["request"],
        "header_menu": get_menu(context),
    }
