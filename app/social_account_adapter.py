from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from app.utils import create_profile


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Override the DefaultSocialAccountAdapter from allauth in order to associate
    the social account with a matching User automatically, skipping the email
    confirm form and existing email error
    """

    def save_user(self, request, sociallogin, form=None):
        """
        Saves a newly signed up social login. In case of auto-signup,
        the signup form is not available.
        """
        user = super().save_user(request, sociallogin, form)
        create_profile(user)
        return user
