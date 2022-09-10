from django.contrib import admin
from .models import Property, PropertyViews


class PropertyAdmin(admin.ModelAdmin):
    """
    ---------------------------
    Property view on admin page
    ---------------------------
    """
    list_display = ('title', 'property_type', 'advert_type', 'price', 'country')
    list_filter = ('property_type', 'advert_type', 'country')


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyViews)
