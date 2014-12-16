from django.views.generic import FormView
from flights.forms import FlightEntryForm

class ProcessFlightView(FormView):
    form_class = FlightEntryForm
    template_name = 'flights/base_flights.html'