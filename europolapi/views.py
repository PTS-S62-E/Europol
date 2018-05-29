from django.shortcuts import render
from rest_framework import viewsets

from europolapi.models import Vehicle
from europolapi.serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
   queryset = Vehicle.objects.all()
   serializer_class = VehicleSerializer