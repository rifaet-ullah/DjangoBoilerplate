from django.shortcuts import render
from django.views import View


class ContactView(View):
    @staticmethod
    def get(request):
        return render(request, "public/contact.html")
