from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Address model with the following attributes:
    number -> address/street number (1 to 9999)
    street -> name of the city (up to 64 char.)
    state -> state's code (up to 2 char.)
    zip_code -> zip code (1 to 99999)
    country_iso_code -> the country's ISO code (>= 3 char.)

    class Meta's verbose_name_plural -> used for the admin
    panel to change the noun to its plural form if needed.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """Letting model with the following attributes:
    title -> a title for the letting (up to 256 char.)
    address -> FK (1to1) of the linked address

    class Meta's verbose_name_plural -> used for the admin
    panel to change the noun to its plural form if needed.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "lettings"
