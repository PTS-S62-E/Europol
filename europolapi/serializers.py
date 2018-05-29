from rest_framework import serializers

from europolapi.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('url', 'HashedLicensePlate', 'serialNumber', 'originCountry')