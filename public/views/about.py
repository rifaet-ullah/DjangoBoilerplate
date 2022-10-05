from django.shortcuts import render
from django.views import View


class AboutView(View):
    @staticmethod
    def get(request):
        return render(request, "public/about.html")
