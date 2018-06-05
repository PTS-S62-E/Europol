from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from europolapi.models import Vehicle
from europolapi.serializers import VehicleSerializer, V1VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('licensePlate', 'serialNumber', 'originCountry')
    search_fields = filter_fields


class V1VehicleViewset(VehicleViewSet):
    serializer_class = V1VehicleSerializer
