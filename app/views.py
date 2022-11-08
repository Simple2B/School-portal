from allauth.account.views import SignupView
from app.forms import CustomUserCreationForm

# from django.core.mail import send_mail


class CustomSignupView(SignupView):
    template_name = "auth_smth/register.html"
    form_class = CustomUserCreationForm

    def post(self, request, *args, **kwargs):
        # TODO implement verification by email
        # form = self.get_form()
        # send_mail('This is the title of the email',
        #         'This is the message you want to send',
        #         'dzhek.layt298@gmail.com',
        #         [
        #             form['email'].value(),
        # # add more emails to this list of you want to
        #         ]
        # )
        return super().post(request, *args, **kwargs)
