from rest_framework import serializers

from europolapi.models import Vehicle


class V1VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('url', 'licensePlate', 'HashedLicensePlate', 'serialNumber', 'originCountry')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('url', 'licensePlate', 'serialNumber', 'originCountry')
