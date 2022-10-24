from django.shortcuts import render
from allauth.account.views import SignupView
from app.forms import CustomUserCreationForm
from django.core.mail import send_mail
# from django.contrib.auth.views import LoginView


class CustomSignupView(SignupView):
    template_name = 'auth_smth/register.html'
    form_class = CustomUserCreationForm

    def post(self, request, *args, **kwargs):
        # form = self.get_form()

        # print(form['email'].value())
        # print('====================================================================================')

        # send_mail('This is the title of the email',
        #         'This is the message you want to send',
        #         'dzhek.layt298@gmail.com',
        #         [
        #             form['email'].value(), # add more emails to this list of you want to
        #         ]
        # )
        return super().post(request, *args, **kwargs)



# class LoginUserView(LoginView):
#     form_class = LoginUserForm
#     template_name = "auth_smth/login_page.html"