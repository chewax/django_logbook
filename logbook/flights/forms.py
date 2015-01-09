from django import forms
from django.forms import ModelForm, inlineformset_factory
from flights.models import Flight, FlightLeg

FlightLegFormset = inlineformset_factory(Flight, FlightLeg, max_num=1)


class FlightEntryForm(ModelForm):
    number = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Flight #'}))

    class Meta:
            model = Flight
            exclude = ['user']