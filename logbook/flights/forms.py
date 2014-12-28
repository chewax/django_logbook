from django import forms
from django.forms import ModelForm, inlineformset_factory
from flights.models import Flight, FlightLeg

FlightLegFormset = inlineformset_factory(Flight, FlightLeg)


class FlightEntryForm(ModelForm):
    number = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Flight Number'}))

    class Meta:
            model = Flight
            fields = ['number']