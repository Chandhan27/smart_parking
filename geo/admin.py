from django.contrib import admin
from .models import ParkingArea

admin.register(ParkingArea)
class ParkingAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude', 'four_wheeler_price', 'two_wheeler_price', 'four_wheeler_available_slots', 'two_wheeler_available_slots')



admin.site.register(ParkingArea, ParkingAreaAdmin) 