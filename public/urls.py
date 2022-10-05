from django.urls import path

from public.views import (
    SignInView,
    SignOutView,
    DashboardView,
    BlogView,
    ContactView,
    AboutView,
)

app_name = "public"
urlpatterns = [
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("blog", BlogView.as_view(), name="blog"),
    path("contact", ContactView.as_view(), name="contact"),
    path("about", AboutView.as_view(), name="about"),
    path("sign-in", SignInView.as_view(), name="sign-in"),
    path("sign-out", SignOutView.as_view(), name="sign-out"),
]
