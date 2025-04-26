from geopy.distance import geodesic
from django.shortcuts import render
from .models import ParkingArea
from django.utils.text import slugify

app_name = 'geo'

def find_parking(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    nearby_slots = []

    if latitude and longitude:
        user_location = (float(latitude), float(longitude))
        for slot in ParkingArea.objects.all():
            parking_location = (slot.latitude, slot.longitude)
            distance = geodesic(user_location, parking_location).km
            if distance <= 5:
                nearby_slots.append({
                    'name': slot.name,
                    'address': slot.address,
                    'latitude': slot.latitude,
                    'longitude': slot.longitude,
                    'distance': distance,
                    'four_wheeler_price': slot.four_wheeler_price,
                    'two_wheeler_price': slot.two_wheeler_price,    
                    'four_wheeler_available_slots': slot.four_wheeler_available_slots,
                    'two_wheeler_available_slots': slot.two_wheeler_available_slots,
                })

    return render(request, 'geo/search_parking.html', {'nearby_slots': nearby_slots})

    
