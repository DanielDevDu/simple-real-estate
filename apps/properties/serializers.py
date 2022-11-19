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
    cover_photo = serializers.SerializerMethodField()
    profile_photo = serializers.SerializerMethodField()
    photo1 = serializers.SerializerMethodField()
    photo2 = serializers.SerializerMethodField()
    photo3 = serializers.SerializerMethodField()
    photo4 = serializers.SerializerMethodField()

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

    def get_cover_photo(self, obj):
        return obj.cover_photo.url

    def get_photo1(self, obj):
        return obj.photo1.url

    def get_photo2(self, obj):
        return obj.photo2.url

    def get_photo3(self, obj):
        return obj.photo3.url

    def get_photo4(self, obj):
        return obj.photo4.url

    def get_profile_photo(self, obj):
        return obj.user.profile.profile_photo.url


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
