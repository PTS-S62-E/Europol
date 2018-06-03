from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from europolapi.models import Vehicle
from europolapi.serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('HashedLicensePlate', 'serialNumber', 'originCountry')
