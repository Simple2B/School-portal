import datetime

from allauth.account.views import SignupView

# from django.core.mail import send_mail
from django.views.generic import View
from django.shortcuts import render

from app.forms import CareersApplyForm, CustomUserCreationForm
from app.models import Career, Candiadate


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


class CareerApplyView(View):
    def get(self, request, *args, **kwargs):
        form = CareersApplyForm()
        context = {"form": form}
        return render(request, "forms/career_apply_form.html", context)

    def post(self, request, *args, **kwargs):
        form = CareersApplyForm(data=request.POST)
        if form.is_valid():
            career_page = Career.objects.first()
            # NOTE in final version form will get career by id sended from template
            # career_page = Career.objects.get(request.POST["career_id"])

            candedate = Candiadate(
                title=form.cleaned_data["full_name"]
                + str(datetime.datetime.timestamp(datetime.datetime.now())),
                full_name=form.cleaned_data["full_name"],
                phone_number=form.cleaned_data["phone_number"],
                email=form.cleaned_data["email"],
                cv=form.cleaned_data["cv"],
                proposal=form.cleaned_data["proposal"],
                career_object=career_page,
            )
            career_page.add_child(instance=candedate)
            career_page.save()
            form = CareersApplyForm()
            return render(request, "forms/career_apply_form.html", {"form": form})
        return render(request, "forms/career_apply_form.html", {"form": form})
