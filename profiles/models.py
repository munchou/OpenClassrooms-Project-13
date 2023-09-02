from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model with the following attributes:
    user -> FK (1to1) of the linked user
    favorite_city -> name of the user's favorite city (up to 64 char.)

    class Meta's verbose_name_plural -> used for the admin
    panel to change the noun to its plural form if needed.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name_plural = "profiles"

    def __str__(self):
        return self.user.username
