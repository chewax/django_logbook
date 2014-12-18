from django import forms
from django.forms import ModelForm, inlineformset_factory
from flights.models import Flight, FlightLeg

class FlightEntryForm(ModelForm):
    number = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Flight Number'}))
    flight_origin_ICAO = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'placeholder': 'From ICAO'}))
    flight_dest_ICAO = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'placeholder': 'To ICAO'}))

    class Meta:
            model = Flight
            fields = ['number', 'flight_origin_ICAO', 'flight_dest_ICAO']

    flight_legs_form = inlineformset_factory(Flight, FlightLeg)