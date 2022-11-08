from app.models import HomePage, Profile, User


def create_profile(user: User) -> None:
    p = Profile(
        name=user.first_name,
        surname=user.last_name,
        age=user.age,
        role="student",
        school_class=user.school_class,
        title=" ".join((user.last_name, user.first_name)),
        slug=user.pk,
    )
    home = HomePage.objects.first()
    home.add_child(instance=p)
    home.save()
