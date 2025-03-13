from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Sponsor(models.Model):
    company_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    spend = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return f'/sponsors'

class SponsorData(models.Model):
    year = models.IntegerField(max_length=255)
    goal = models.DecimalField(max_digits=15, decimal_places=2)
    in_kind = models.DecimalField(max_digits=15, decimal_places=2)
    in_cash = models.DecimalField(max_digits=15, decimal_places=2)