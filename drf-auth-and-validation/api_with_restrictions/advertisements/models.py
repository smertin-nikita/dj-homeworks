from django.conf import settings
from django.db import models
from django.db.models import Q


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )

    draft = models.BooleanField(default=False)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='advertisements'
    )

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='UsersAdvertisements',
        related_name='favorites')

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class UsersAdvertisements:

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q('advertisement__creator' == 'user'),
                name='no_creator',
            ),
        ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    advertisements = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

