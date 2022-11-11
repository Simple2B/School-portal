from django import template
from wagtail.models import Site


register = template.Library()


def get_menu(context):
    """Function for header and footer. Returns menu items"""
    return (
        Site.find_for_request(context["request"])
        .root_page.get_children()
        .live()
        .in_menu()
    )
