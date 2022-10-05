import re

from django import forms

from public.models import Account


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
        exclude = ("username", "date_joined", "password_salt")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise forms.ValidationError(
                "Password length must be at least 6 character long"
            )
        if not re.compile(r".*[a-z]+.*").match(password):
            raise forms.ValidationError(
                "Password must contain at least one lowercase letter"
            )
        if not re.compile(r".*[A-Z]+.*").match(password):
            raise forms.ValidationError(
                "Password must contain at least one uppercase letter"
            )
        if not re.compile(r".*[0-9]+.*").match(password):
            raise forms.ValidationError("Password must contain at least one digit")
        return password
