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