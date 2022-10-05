from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from public.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("public/", include("public.urls", namespace="public")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
