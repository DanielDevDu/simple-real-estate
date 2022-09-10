"""
----------------
Property module
----------------
"""

from email.policy import default
from django.db import models
import random
import string
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class PropertyPyblishedManager(models.Manager):
    """
    -----------------------------
    Get all published properties
    with is_published=True
    -----------------------------
    """

    def get_queryset(self):
        return (
            super(PropertyPyblishedManager, self)
            .get_queryset().filter(is_published=True)
        )


class Property(TimeStampedUUIDModel):
    """
    ---------------
    Property model
    ---------------
    """

    class AdveertType(models.TextChoices):
        """
        ----------------
        Action types
        ----------------
        """
        FOR_SALE = "For sale", _("For Sale")
        FOR_RENT = "For rent", _("For Rent")
        AUCTION = "Auction", _("Auction")

    class PropertyType(models.TextChoices):
        """
        ----------------
        Property types
        ----------------
        """
        HOUSE = "House", _("House")
        APARTMENT = "Apartment", _("Apartment")
        OFFICE = "Oficce", _("Oficce")
        COMMERCIAL = "Commercial", _("Commercial")
        WAREHOUSE = "Warehouse", _("Warehouse")
        OTHER = "Other", _("Other")

    user = models.ForeignKey(
        User,
        verbose_name=_("Agent, Seller or buyer"),
        related_name="agent_buyer",
        on_delete=models.DO_NOTHING
    )
    title = models.CharField(
        verbose_name=_("Property Title"),
        max_length=255
    )
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    ref_code = models.CharField(verbose_name=_("Property Reference Code"), max_length=255, unique=True, blank=True)
    description = models.TextField(verbose_name=_("Property Description"),
                                   default="Default description... update me...", blank=True)
    country = CountryField(verbose_name=_("Country"), default="CO", blank_label="(Select Country)")
    city = models.CharField(verbose_name=_("City"), max_length=255, default="Bogotá")
    postal_code = models.CharField(verbose_name=_("Postal Code"), max_length=100, default="110221")
    stree_address = models.CharField(verbose_name=_("Street Address"), max_length=150, default="Calle 100 # 10 - 10")
    property_number = models.IntegerField(
        verbose_name=_("Property Number"),
        validators=[MinValueValidator(1)], default=112
    )
    price = models.DecimalField(
        verbose_name=_("Price"), max_digits=8, decimal_places=2, default=0.00
    )
    tax = models.DecimalField(
        verbose_name=_("Tax"), max_digits=6, decimal_places=2, default=0.15,
        help_text=_("15% property tex charged")
    )
    plot_area = models.DecimalField(
        verbose_name=_("Plot Area(m^2)"), max_digits=8, decimal_places=2, default=0.00
    )
    total_floors = models.IntegerField(
        verbose_name=_("Number of Floors"), default=0
    )
    bedrooms = models.IntegerField(
        verbose_name=_("Number of Bedrooms"), default=1
    )
    bathrooms = models.DecimalField(
        verbose_name=_("Number of Bathrooms"), max_digits=4,
        default=1, decimal_places=2
    )
    advert_type = models.CharField(
        verbose_name=_("Advert Type"), max_length=50,
        choices=AdveertType.choices, default=AdveertType.FOR_SALE
    )
    property_type = models.CharField(
        verbose_name=_("Property Type"), max_length=50,
        choices=PropertyType.choices, default=PropertyType.OTHER
    )
    cover_photo = models.ImageField(
        verbose_name=_("Main photo"),
        default="/house_sample.jpeg",
        null=True, blank=True
    )
    photo1 = models.ImageField(
        default="interior_sample.jpeg",
        null=True, blank=True
    )
    photo2 = models.ImageField(
        default="interior_sample.jpeg",
        null=True, blank=True
    )
    photo3 = models.ImageField(
        default="interior_sample.jpeg",
        null=True, blank=True
    )
    photo4 = models.ImageField(
        default="interior_sample.jpeg",
        null=True, blank=True
    )
    published_status = models.BooleanField(
        verbose_name=_("Published Status"), default=False
    )
    views = models.IntegerField(
        verbose_name=_("Total Views"),
        default=0
    )

    objects = models.Manager()
    published = PropertyPyblishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def save(self, *args, **kwargs):
        """
        ----------------
        Save property
        ----------------
        """
        self.title = str.title(self.title)
        self.description = str.capitalize(self.description)
        self.ref_code = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property_price(self):
        """
        ----------------
        Get final price
        ----------------
        """
        tax_percentage = self.tax
        property_price = self.price
        tax_amount = round(tax_percentage * property_price, 2)
        price_after_tax = float(round(property_price + tax_amount, 2))
        return price_after_tax


class PropertyViews(TimeStampedUUIDModel):
    """
    ----------------
    Property views
    ----------------
    """

    property = models.ForeignKey(
        Property, verbose_name=_("Property"),
        on_delete=models.CASCADE,
        related_name="property_views"
    )
    ip = models.GenericIPAddressField(
        verbose_name=_("IP Address")
    )

    def __str__(self):
        return f"Total views on - {self.property.title} is {self.property.views} views(s)"

    class Meta:
        verbose_name = _("Total Views on Property")
        verbose_name_plural = _("Total Property Views")
