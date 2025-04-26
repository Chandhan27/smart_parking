from django.db import models

class ParkingArea(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    four_wheeler_price = models.CharField(max_length=10, default='FREE', blank=True)
    two_wheeler_price = models.CharField(max_length=10, default='FREE', blank=True)
    four_wheeler_available_slots = models.IntegerField(default=0)
    two_wheeler_available_slots = models.IntegerField(default=0)

    
    def __str__(self):
        return self.name
