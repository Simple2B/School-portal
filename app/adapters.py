
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from django.core.mail import send_mail
from django.contrib.auth import get_user_model


class CustomAdapter(DefaultAccountAdapter): pass
    # def get_email_confirmation_url(self, request, emailconfirmation):
    #     """Constructs the email confirmation (activation) url.
    #     Note that if you have architected your system such that email
    #     confirmations are sent outside of the request context `request`
    #     can be `None` here.
    #     """
    #     url = "http://127.0.0.1:8000/confirm-email/" + emailconfirmation.key
    #     return url




from app.models import HomePage, Profile



class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Override the DefaultSocialAccountAdapter from allauth in order to associate
    the social account with a matching User automatically, skipping the email
    confirm form and existing email error
    """
    # def pre_social_login(self, request, sociallogin):
    #     from django.contrib.auth import get_user_model
    #     User = get_user_model()
        
    #     user = User.objects.filter(email=sociallogin.user.email).first()
    #     if user and not sociallogin.is_existing:
    #         sociallogin.connect(request, user)

    def save_user(self, request, sociallogin, form=None):
        """
        Saves a newly signed up social login. In case of auto-signup,
        the signup form is not available.
        """
        user = super().save_user(request, sociallogin, form)
        p = Profile(name=user.first_name, surname=user.last_name, age=user.age, role='student', school_class=user.school_class, 
                            title=' '.join((user.last_name, user.first_name)), slug=user.pk)
        home = HomePage.objects.first()
        home.add_child(instance=p)
        home.save()
        return user
