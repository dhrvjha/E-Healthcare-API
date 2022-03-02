from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class Staff(AbstractUser):
    class Gender(models.TextChoices):
        MAL = "1", "MALE"
        FEM = "2", "FEMALE"
        TRAN = "3", "TRANS"
        GAY = "4", "GAY"
        DTS = "5", "DECLINE TO STATE"

    class Position(models.TextChoices):
        BRAIN_SURGON = "1"
        HEART_SURGON = "2"
        NURSE = "3"
        INTERN = "4"

    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.DTS)
    position = models.CharField(
        max_length=3, choices=Position.choices, default=Position.INTERN
    )
