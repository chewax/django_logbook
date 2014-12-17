from django.core.urlresolvers import reverse
from django.views.generic import FormView, CreateView
from flights.forms import FlightEntryForm

class ProcessFlightView(CreateView):
    form_class = FlightEntryForm
    template_name = 'flights/base_flights.html'
    success_url = '/'


    def form_valid(self, form):
        flt = form.save()
        return super(ProcessFlightView, self).form_valid(form)