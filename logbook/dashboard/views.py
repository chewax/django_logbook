from django.views.generic import TemplateView
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import timedelta, datetime
import json

from core.views import CurrencyAsideMixin
from flights.models import Flight


class DashboardProcessView(TemplateView, CurrencyAsideMixin):
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
                result_set = Flight.objects.filter(q)
            else:
                result_set = Flight.objects.filter(user=user)
        else:
            result_set = Flight.objects.filter(user=user)

        # Add Pagination
        paginator = Paginator(result_set, 13) #Show 15 Flights
        page = self.request.GET.get('page')
        try:
            flights = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            flights = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last
            #  page of results.
            flights = paginator.page(paginator.num_pages)

        context['flights'] = flights
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, **kwargs)


class FlightData(View):

    def get_all_time_data(self):
        """
        Retrieves flown hours for all time. Accumulated
        :return: List of dictionaries.
        """
        data = []
        accumulated_time = 0

        #TODO Retrieve this values from user settings
        limit = 90

        # Get all flights
        for flight in Flight.objects.filter(user=self.request.user).\
                order_by('flightleg__time_out'):
            hours = round(float(flight.flight_time.seconds)/3600, 2)
            accumulated_time += hours
            data.append({
                "date": flight.date.isoformat(),
                "time": accumulated_time,
                "limit": limit,
            })
        return data

    def get_last_30_days(self):
        """
        Retrieves flown hours of last 30 days. Accumulated
        :return: List of dictionaries.
        """
        data = []
        accumulated_time = 0
        #TODO Retrieve this values from user settings
        limit = 120

        # Construct the starting date to be considered
        start_date = datetime.today() + timedelta(days=-30)

        for flight in Flight.objects.filter(user=self.request.user).\
                order_by('flightleg__time_out').\
                filter(flightleg__time_out__gte=start_date):
            hours = round(float(flight.flight_time.seconds)/3600, 2)
            accumulated_time += hours
            data.append({
                "date": flight.date.isoformat(),
                "time": accumulated_time,
                "limit": limit
            })
        return data

    def get_last_90_days(self):
        """
        Retrieves flown hours of last 90 days. Accumulated
        :return: List of dictionaries.
        """
        data = []
        accumulated_time = 0
        #TODO Retrieve this values from user settings
        limit = 300

        # Construct the starting date to be considered
        start_date = datetime.today() + timedelta(days=-90)

        for flight in Flight.objects.filter(user=self.request.user).\
                order_by('flightleg__time_out').\
                filter(flightleg__time_out__gte=start_date):
            hours = round(float(flight.flight_time.seconds)/3600, 2)
            accumulated_time += hours
            data.append({
                "date": flight.date.isoformat(),
                "time": accumulated_time,
                "limit": limit
            })
        return data

    def get_last_12_months(self):
        """
        Retrieves flown hours of last 12 consecutive months. Accumulated
        :return: List of dictionaries.
        """
        data = []
        accumulated_time = 0
        #TODO Retrieve this values from user settings
        limit = 1000

        # Construct the starting date to be considered
        target_year = datetime.today().year - 1
        current_month = datetime.today().month
        start_date = datetime(year=target_year, month=current_month, day=1)

        for flight in Flight.objects.filter(user=self.request.user).\
                order_by('flightleg__time_out').\
                filter(flightleg__time_out__gte=start_date):
            hours = round(float(flight.flight_time.seconds)/3600, 2)
            accumulated_time += hours
            data.append({
                "date": flight.date.isoformat(),
                "time": accumulated_time,
                "limit": limit
            })
        return data

    def get_current_month(self):
        """
        Retrieves flown hours of current month. Accumulated
        :return: List of dictionaries.
        """
        current_year = datetime.today().year
        current_month = datetime.today().month
        data = []

        accumulated_time = 0
        #TODO Retrieve this values from user settings
        limit = 90

        for flight in Flight.objects.filter(user=self.request.user).\
                order_by('flightleg__time_out').\
                filter(flightleg__time_out__year=current_year,
                       flightleg__time_out__month=current_month):
            hours = round(float(flight.flight_time.seconds)/3600, 2)
            accumulated_time += hours
            data.append({
                "date": flight.date.isoformat(),
                "time": accumulated_time,
                "limit": limit,
            })

        return data


    def get_last_calendar_year(self):
        """
        Retrieves flown hours of last calendar year. Accumulated
        :return: List of dictionaries.
        """
        target_year = datetime.today().year - 1
        data = []

        accumulated_time = 0
        #TODO Retrieve this values from user settings
        limit = 1000

        for flight in Flight.objects.filter(user=self.request.user).\
                order_by('flightleg__time_out').\
                filter(flightleg__time_out__year=target_year):
            hours = round(float(flight.flight_time.seconds)/3600, 2)
            accumulated_time += hours
            data.append({
                "date": flight.date.isoformat(),
                "time": accumulated_time,
                "limit": limit,
            })

        return data

    def get_current_calendar_year(self):
        """
        Retrieves flown hours of last calendar year. Accumulated
        :return: List of dictionaries.
        """
        target_year = datetime.today().year
        data = []

        accumulated_time = 0
        #TODO Retrieve this values from user settings
        limit = 1000

        for flight in Flight.objects.filter(user=self.request.user).\
                order_by('flightleg__time_out').\
                filter(flightleg__time_out__year=target_year):
            hours = round(float(flight.flight_time.seconds)/3600, 2)
            accumulated_time += hours
            data.append({
                "date": flight.date.isoformat(),
                "time": accumulated_time,
                "limit": limit,
            })

        return data

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
        retrieve = self.request.POST["retrieve"]
        if retrieve == 'at':
            data = self.get_all_time_data()

        elif retrieve == '1m':
            data = self.get_current_month()

        elif retrieve == '30d':
            data = self.get_last_30_days()

        elif retrieve == '90d':
            data = self.get_last_90_days()

        elif retrieve == '1y':
            data = self.get_last_calendar_year()

        elif retrieve == '12m':
            data = self.get_last_12_months()

        elif retrieve == 'cy':
            data = self.get_current_calendar_year()

        return HttpResponse(json.dumps(data))

