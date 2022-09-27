"""
-------------------------
Serialize Profile Model
-------------------------
"""
from django_countries.serializer_fields import CountryField
from rest_framework import serializers

# My models
from .models import Enquiry


class EnquirySerializer(serializers.ModelSerializer):
    """
    ----------------
    Enquiry Serializer
    ----------------
    """

    class Meta:
        model = Enquiry
        fileds = "__all__"
