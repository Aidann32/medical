from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    DOCTOR = 1
    CLIENT = 2  

    ROLE_CHOICES = (
        (DOCTOR, 'Doctor'),
        (CLIENT, 'Client'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    confirmed = models.BooleanField(verbose_name='Подтвержден', default=True)

