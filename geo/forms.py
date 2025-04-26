from django import forms

class LocationForm(forms.Form):
    latitude = forms.FloatField(label="Your Latitude")
    longitude = forms.FloatField(label="Your Longitude")
