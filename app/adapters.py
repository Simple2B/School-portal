
from allauth.account.adapter import DefaultAccountAdapter
from django.core.mail import send_mail


class CustomAdapter(DefaultAccountAdapter): pass
    # def get_email_confirmation_url(self, request, emailconfirmation):
    #     """Constructs the email confirmation (activation) url.
    #     Note that if you have architected your system such that email
    #     confirmations are sent outside of the request context `request`
    #     can be `None` here.
    #     """
    #     url = "http://127.0.0.1:8000/confirm-email/" + emailconfirmation.key
    #     return url
