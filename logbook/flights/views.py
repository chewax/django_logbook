from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, UpdateView
from core.views import CurrencyAsideMixin

from flights.forms import FlightEntryForm, FlightLegFormset
from flights.models import Flight


class ProcessFlightView(CreateView, CurrencyAsideMixin):
    form_class = FlightEntryForm
    # TODO Use Reverse
    template_name = 'flights/add_flight.html'
    success_url = '/flights/new'

    def get_context_data(self, **kwargs):
        """
        Add inline formset (Flight Legs) to context data
        :param kwargs:
        :return: context (dict)
        """
        context = super(ProcessFlightView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['flight_legs'] = FlightLegFormset(self.request.POST)
        else:
            context['flight_legs'] = FlightLegFormset()
        return context

    def form_valid(self, form):
        """
        Validate the form(Flight) and the inline formset(Flight Legs)
        If both are valid. Asociate with logged user and save them
        :param form:
        :return: HttpResponse
        """
        context = self.get_context_data()
        leg_formset = context['flight_legs']

        if leg_formset.is_valid():
            #First save the form to get the model objects
            flight = form.save()

            #Asociate logged user to flight
            flight.user = self.request.user
            flight.save()

            #Asociate fomset to flight
            leg_formset.instance = flight
            leg_formset.save()
            return redirect(reverse('flights:new'))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ProcessFlightDeletion(DeleteView, CurrencyAsideMixin):
    success_url = '/dashboard/'
    model = Flight


class ProcessFlightUpdate(UpdateView, CurrencyAsideMixin):
    success_url = '/dashboard/'
    form_class = FlightEntryForm
    model = Flight

    def get_context_data(self, **kwargs):
        """
        Add inline formset (Flight Legs) to context data
        :param kwargs:
        :return: context (dict)
        """
        context = super(ProcessFlightUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['flight_legs'] = FlightLegFormset(self.request.POST,
                                                      instance=self.object)
        else:
            context['flight_legs'] = FlightLegFormset(instance=self.object)
            print(self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        leg_formset = context['flight_legs']

        if leg_formset.is_valid():
            # First save the form to get the model objects
            flight = form.save()

            # Asociate logged user to flight
            flight.user = self.request.user
            flight.save()

            # Asociate fomset to flight
            leg_formset.instance = flight
            leg_formset.save()
            return redirect(reverse('dashboard:user_dashboard'))
        else:
            return self.render_to_response(self.get_context_data(form=form))