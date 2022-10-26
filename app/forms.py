from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm
from app.models import SchoolClassPage, User, Profile, HomePage

from app.utils import create_profile


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, label=_("First name"))
    last_name = forms.CharField(required=True, label=_("Last name"))
    age = forms.CharField(required=True, label=_("Age"))
    school_class = forms.ModelChoiceField(queryset=SchoolClassPage.objects.all(), required=True, label=_("Your class"))

    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ('is_superuser',)
        fields = ('username', 'email','first_name','last_name', 'school_class', 'age')

    def save(self, commit=True):
        user = super().save(commit=True)
        create_profile(user)
        return user
