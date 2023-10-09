from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Thing(models.Model):
    name = models.CharField(
        max_length = 30,
        unique = True,
        blank = False)
    
    description = models.TextField(
        max_length = 120, 
        blank = True,
        unique = False
    )

    quantity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        unique = False
    )

    def __str__(self):
        return self.name
