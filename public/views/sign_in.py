from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views import View


class SignInView(View):
    @staticmethod
    def post(request):
        if request.user.is_authenticated:
            return redirect("public:dashboard")
        user = authenticate(
            request,
            email=request.POST.get("email"),
            password=request.POST.get("password"),
        )
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully signed in")
            return redirect("public:dashboard")
        messages.error(request, "Invalid username or password")
        return redirect("index")
