from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    DOCTOR = 1
    NURSE = 2  

    ROLE_CHOICES = (
        (DOCTOR, 'Doctor'),
        (NURSE, 'Nurse'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

