from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class DashboardView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "public/dashboard.html")
