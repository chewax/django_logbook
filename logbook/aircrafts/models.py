from django.db import models

from accounts.models import User

class AircraftType(models.Model):
    # eg: BOEING
    factory = models.CharField(max_length=50, blank=False, null=False,
                               verbose_name="Manufacturer")
    # eg: B767
    original_release = models.CharField(max_length=10, blank=False, null=False,
                                        verbose_name="Model")
    # eg: 300
    update_number = models.CharField(max_length=10, blank=True, null=True,
                                     verbose_name="Version")
    # B763
    short_name = models.CharField(max_length=4, blank=False, null=False,
                                  verbose_name="Short")
    # Boeing 767-300
    description = models.TextField(blank=True, null=True,
                                   verbose_name="Description")


    def __str__(self):
        return self.short_name

class Aircraft(models.Model):
    user = models.ForeignKey(User, null=True)
    reg_number = models.CharField(max_length=10, blank=False, null=False)
    model = models.ForeignKey(AircraftType)

    def __str__(self):
        return self.reg_number

