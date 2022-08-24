#!/env/bin/python3
"""
--------------------------------
Define config to admin Users App
--------------------------------
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    """
    ------------------
    Custom User Admin
    ------------------
    """

    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["id", "email", "first_name", "last_name", "username", "is_staff", "is_active"]
    list_display_links = ["id", "email"]
    list_filter = ["email", "username", "first_name", "last_name", "is_staff", "is_active"]
    fieldsets = (
        (
            _("Login Credentials"),
            {"fields": ("email", "password")},
        ),
        (
            _("Personal Information"),
            {
                "fields": ("username", "first_name", "last_name")
            }
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")
            }
        ),
        (
            _("Important Dates"),
            {
                "fields": ("last_login", "date_joined")
            }
        )
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active"),
        },),
    )
    search_fields = ["email", "username", "first_name", "last_name"]

admin.site.register(User, UserAdmin)