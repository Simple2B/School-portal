from django import forms
from django.utils.translation import gettext_lazy
from django import forms

from wagtail.users.forms import UserCreationForm
from app.models import SchoolClassPage, User

from app.utils import create_profile


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, label=gettext_lazy("First name"))
    last_name = forms.CharField(required=True, label=gettext_lazy("Last name"))
    age = forms.CharField(required=True, label=gettext_lazy("Age"))
    school_class = forms.ModelChoiceField(
        queryset=SchoolClassPage.objects.all(),
        required=True,
        label=gettext_lazy("Your class"),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ("is_superuser",)
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "school_class",
            "age",
        )

    def save(self, commit=True):
        user = super().save(commit=True)
        create_profile(user)
        return user


# class CareersApplyForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'phone', 'email',)
