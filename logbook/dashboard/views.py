from django.views.generic import TemplateView
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers

import json

from flights.models import Flight


class DashboardProcessView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        """
        Recovers context data depending on the filters submitted by the user
        :param kwargs:
        :return: Context
        """
        context = super(DashboardProcessView, self).get_context_data(**kwargs)
        append_context = []
        user = self.request.user
        if self.request.method == 'POST':
            input_query = self.request.POST["query_input"]
            print('input_query = {}'.format(input_query))

            if input_query:
                q = Q(aircraft__reg_number__contains=input_query) \
                    | Q(aircraft__model__short_name__contains=input_query) \
                    | Q(number__contains=input_query) \
                    | Q(flightleg__departure_airport__contains=input_query) \
                    | Q(flightleg__arrival_airport__contains=input_query)

                q = q & Q(user=user)

                # TODO Add Distinct to this query -- .distinct('pk')
                # It is currently not supported by the database backend
                context['flights'] = Flight.objects.filter(q)
            else:
                context['flights'] = Flight.objects.filter(user=user)
        else:
            context['flights'] = Flight.objects.filter(user=user)

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, **kwargs)


class FlightData(View):

    def post(self, request):
        """
        Computes various statistic parameters of flight time. Such as,
        accumulated time in last 30 days, 90 days and 365 days. Limits and
        daily flight time. Is thought to be consumed with ajax request:

        eg.:
        $.ajax({url:"/dashboard/get_flight_data/", type:"POST", dataType:"json"
        , async:false});

        :param request: HttpRequest
        :return: HttpResponse with JSON.
        """
        data = []
        accumulated_time = 0
        #TODO Retrieve this values from user settings
        limit_30 = 90
        limit_90 = 240
        limit_365 = 1000
        for flight in Flight.objects.filter(user=self.request.user).order_by('flightleg__time_out'):
            hours = float(flight.flight_time.seconds)/3600
            accumulated_time += hours
            data.append({
                "date": "{}-{}-{}".format(flight.date.year, flight.date.month, flight.date.day),
                "daily_time": hours,
                "accumulated_time": accumulated_time,
                "limit_30": limit_30,
                "limit_90": limit_90,
                "limit_365": limit_365
            })

        return HttpResponse(json.dumps(data))

