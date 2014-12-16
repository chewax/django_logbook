from django.forms import ModelForm
from flights.models import Flight

class FlightEntryForm(ModelForm):
    class Meta:
            model = Flight
            fields = ['number']
