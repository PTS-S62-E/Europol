from django.db import models


# Create your models here.
class Vehicle(models.Model):
    HashedLicensePlate = models.TextField(max_length=64, default="")
    serialNumber = models.TextField(max_length=128, default="", primary_key=True)
    originCountry = models.TextField(max_length=64, default="")

    def __str__(self):
        return "{0} from {1}".format(self.HashedLicensePlate, self.originCountry)


