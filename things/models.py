from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
