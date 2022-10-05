import random
import uuid
from string import ascii_letters, digits

from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from public.forms import RegistrationForm
from public.views.utils import form_errors


class IndexView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect("public:dashboard")
        return render(request, "public/index.html")

    @staticmethod
    def post(request):
        if request.POST.get("password") != request.POST.get("confirm-password"):
            messages.error(request, "Password and confirm password did not matched")
        else:
            form = RegistrationForm(
                data={
                    "first_name": request.POST.get("first-name"),
                    "last_name": request.POST.get("last-name"),
                    "email": request.POST.get("email"),
                    "password": request.POST.get("password"),
                }
            )

            if form.is_valid():
                account = form.save(commit=False)
                account.username = uuid.uuid4()
                account.password_salt = "".join(
                    random.choices(ascii_letters + digits, k=random.randint(10, 20))
                )
                account.password = make_password(
                    password=form.cleaned_data.get("password"),
                    salt=account.password_salt,
                )
                account.is_active = True
                account.save()
                messages.success(
                    request, "Registration successful. Please try to sign in."
                )
            else:
                for error in form_errors(form):
                    messages.error(request, error)

        return redirect("index")
