from django.forms import ModelForm, modelformset_factory, inlineformset_factory
from flights.models import Flight, FlightLeg

class FlightEntryForm(ModelForm):

    class Meta:
            model = Flight
            fields = ['number', 'flight_origin_ICAO', 'flight_dest_ICAO']

    flight_legs_form = inlineformset_factory(Flight, FlightLeg)