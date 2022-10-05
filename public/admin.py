from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "username",
        "email",
        "date_joined",
        "is_staff",
        "is_active",
        "is_superuser",
    )
