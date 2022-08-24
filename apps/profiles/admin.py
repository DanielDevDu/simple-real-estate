from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    -------------------------
    Custom View Profile Admin
    -------------------------
    """

    list_display = ["id", "pkid", "user", "phone_number", "gender", "country", "city"]
    list_filter = ["gender", "country", "city"]
    list_display_links = ["id", "pkid", "user"]


admin.site.register(Profile, ProfileAdmin)
