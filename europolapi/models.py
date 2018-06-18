import uuid
import hashlib
from django.db import models


class Vehicle(models.Model):
    licensePlate = models.TextField(max_length=64, default="", blank=True)
    serialNumber = models.TextField(default=uuid.uuid4(), max_length=64, primary_key=True)
    originCountry = models.TextField(max_length=2, default="")

    def HashedLicensePlate(self):
        return hashlib.md5(self.licensePlate.encode()).hexdigest()

    def __str__(self):
        return "{0} from {1}".format(self.licensePlate, self.originCountry)
