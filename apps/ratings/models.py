#!/env/bin/python3
"""
------------------------------
Define Ratings class
------------------------------
"""
from tabnanny import verbose
import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# My models
from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile
from real_estate.settings.base import AUTH_USER_MODEL


class Rating(TimeStampedUUIDModel):
    """
    -------------
    Ratings model
    -------------
    """

    class Range(models.IntegerChoices):
        """
        -------------
        Ratings range
        -------------
        """
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("User providing rating"),
        null=True
    )
    agent = models.ForeignKey(
        Profile,
        verbose_name=_("Agent being rated (profile)"),
        on_delete=models.CASCADE,
        related_name="agent_review",
        null=True
    )
    rating = models.IntegerField(
        choices=Range.choices,
        verbose_name=_("Rating"),
        help_text="1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent",
        default=0
    )
    comment = models.TextField(verbose_name=_("Comment"))

    def __str__(self):
        return f"{self.agent} rated at {self.rating}"

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')
        unique_together = ('rater', 'agent')
