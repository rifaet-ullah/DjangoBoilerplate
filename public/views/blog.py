from django.shortcuts import render
from django.views import View


class BlogView(View):
    @staticmethod
    def get(request):
        return render(request, "public/blog.html")
