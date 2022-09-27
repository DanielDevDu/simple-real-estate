"""
----------------
Enquiries module
----------------
"""

from email.policy import default
from sqlite3 import Time

from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel


class Enquiry(TimeStampedUUIDModel):
    """
    Enquiry model
    """

    name = models.CharField(_("Your name"), max_length=100)
    phone_number = PhoneNumberField(
        _("Phone number"), max_length=30, default="+573196798262"
    )
    email = models.EmailField(_("Email"))
    subject = models.CharField(_("Subject"), max_length=100)
    message = models.TextField(_("Message"))

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = _("Enquiry")
        verbose_name_plural = _("Enquiries")
