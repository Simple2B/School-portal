from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm
from .models import SchoolClassPage, User, Profile, HomePage

# class CustomUserEditForm(UserEditForm):
#     country = forms.CharField(required=True, label=_("Country"))
#     status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))


class CustomUserCreationForm(UserCreationForm):
    # username = forms.CharField(required=True, label=_("Username"))
    first_name = forms.CharField(required=True, label=_("First name"))
    last_name = forms.CharField(required=True, label=_("Last name"))
    age = forms.CharField(required=True, label=_("Age"))
    school_class = forms.ModelChoiceField(queryset=SchoolClassPage.objects.all(), required=True, label=_("Your class"))

    class Meta(UserCreationForm.Meta):
        model = User
        # exclude = ('is_superuser',)
        fields = ('username', 'email','first_name','last_name', 'school_class', 'age')

    # @property
    # def username(self):
    #     return self.first_name + " " + self.last_name

    def save(self, commit=True):
        user = super().save(commit=True)
        p = Profile(name=user.first_name, surname=user.last_name, age=user.age, role='student', school_class=user.school_class, 
                                    title=' '.join((user.last_name, user.first_name)), slug=user.pk)
        home = HomePage.objects.first()
        home.add_child(instance=p)
        home.save()
        return user
