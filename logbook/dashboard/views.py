from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, TemplateView
from flights.forms import FlightEntryForm, FlightLegFormset
from flights.models import Flight, FlightLeg


class DashboardProcessView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    # model = Flight

    def get_context_data(self, **kwargs):
        context = super(DashboardProcessView, self).get_context_data(**kwargs)
        append_context = []
        user = self.request.user
        context['flights'] = Flight.objects.filter(user=user)
        return context



class DashboardProcessView_future(CreateView):
    form_class = FlightEntryForm
    template_name = 'dashboard/dashboard.html'
    success_url = 'dashboard/dashboard.html'


    def get_context_data(self, **kwargs):
        """
        Add inline formset (Flight Legs) to context data
        :param kwargs:
        :return: context (dict)
        """
        context = super(DashboardProcessView_future, self).get_context_data(**kwargs)
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
            return redirect('dashboard/dashboard.html')
        else:
            return self.render_to_response(self.get_context_data(form=form))