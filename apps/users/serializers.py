"""
--------------------------
Serializers to User Model
--------------------------
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    --------------------------------
    Class that serialize User model
    --------------------------------
    """

    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_numer")
    profile_photo = serializers.ImageField(source="profile.profile_photo")
    city = serializers.CharField(source="profile.city")
    top_seller = serializers.BooleanField(source="profile.top_seller")
    full_name = serializers.SerializerMethodField(source="get_full_name")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "full_name",
                  "gender", "phone_number", "profile_photo", "city", "top_seller"]

    def get_first_name(self, obj):
        return obj.first_name

    def get_last_name(self, obj):
        return obj.last_name

    def to_representation(self, instance):
        """
        -------------------------------------------------------
        Custom representation of the user model serialization
        -------------------------------------------------------
        """
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["is_admin"] = True
        return representation


class CreateUserSerializer(UserCreateSerializer):
    """
    -------------------------------------------------------
    Class that serialize User model for creation
    -------------------------------------------------------
    """
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
