from wagtail.models import Site, Locale
from app.models import HomePage, Profile, User, FormPage


def create_profile(user: User) -> None:
    p = Profile(
        name=user.first_name,
        surname=user.last_name,
        age=user.age,
        role="student",
        school_class=user.school_class,
        title=" ".join((user.last_name, user.first_name)),
        slug=user.pk,
        email=user.email,
    )
    home = HomePage.objects.first()
    home.add_child(instance=p)
    home.save()


def get_menu(context):
    """Function for header and footer. Returns menu items"""
    current_home_page = Site.find_for_request(context["request"]).root_page.localized
    menu = [current_home_page]
    [menu.append(item) for item in current_home_page.get_children().live().in_menu()]
    return menu
