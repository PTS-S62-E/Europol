from django.contrib import admin

# Register your models here.
from europolapi.models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    allfields = ('HashedLicensePlate', 'serialNumber', 'originCountry')
    list_display = allfields
    list_display_links = allfields
    search_fields = allfields


admin.site.register(Vehicle, VehicleAdmin)
