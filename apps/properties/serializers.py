"""
-------------------------
Serialize Property Model
-------------------------
"""
from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

# My models
from .models import Property, PropertyViews


class PropertySerializer(serializers.ModelSerializer):
    """
    ----------------
    Property Serializer
    ----------------
    """
    country = CountryField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Property
        # fields = '__all__'
        exclude = ["pkid", "updated_at"]

    def get_user(self, obj):
        """
        ----------------------
        Get username from user
        ----------------------
        """
        return obj.user.username


class PropertyCreateSerializer(serializers.ModelSerializer):
    """
    ----------------
    Property Serializer
    ----------------
    """
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        exclude = ["pkid", "updated_at"]


class PropertyViewsSerializer(serializers.ModelSerializer):
    """
    ----------------
    Property Views Serializer
    ----------------
    """
    class Meta:
        model = PropertyViews
        exclude = ["pkid", "updated_at"]
