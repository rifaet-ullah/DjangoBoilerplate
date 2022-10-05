from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class SignOutView(View):
    @staticmethod
    def post(request):
        logout(request)
        messages.success(request, "Successfully signed out the user")
        return redirect("index")
