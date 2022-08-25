from django.contrib import admin
from .models import Rating


class RatingAdmin(admin.ModelAdmin):
    """
    -------------------------
    Custom View Rating Admin
    -------------------------
    """

    list_display = ["rater", "agent", "rating"]
    list_filter = ["rating"]


admin.site.register(Rating, RatingAdmin)
