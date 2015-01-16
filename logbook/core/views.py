from datetime import datetime, timedelta

from django.contrib.auth import get_user
from django.views.generic.base import ContextMixin

from flights.models import Flight


class CurrencyCalculator():

    def add_months(self, d, x):
        new_month = (((d.month - 1) + x) % 12) + 1
        new_year = d.year + ((( d.month - 1) + x) / 12)
        return datetime(year=new_year, month=new_month, day=d.day)

    def get_all_time_data(self, user):
        """
        Retrieves flown hours for all time. Accumulated
        :return: Integer Time
        """
        accumulated_time = 0
        # Get all flights
        for flight in Flight.objects.filter(user=user). \
                order_by('flightleg__time_out'):
            hours = round(float(flight.flight_time.seconds) / 3600, 2)
            accumulated_time += hours
        return accumulated_time

    def get_flight_last_x_time(self, user, day_delta=0, month_delta=0):
        """
        Retrieves flown hours of last 30 days. Accumulated
        :return: Integer Time
        """
        accumulated_time = 0

        # Construct the starting date to be considered

        start_date = datetime.today()

        if month_delta:
            start_date = self.add_months(start_date, -month_delta)

        start_date = start_date + timedelta(days=-day_delta)

        for flight in Flight.objects.filter(user=user). \
                order_by('flightleg__time_out'). \
                filter(flightleg__time_out__gte=start_date):
            hours = round(float(flight.flight_time.seconds) / 3600, 2)
            accumulated_time += hours

        return accumulated_time

    def get_service_last_x_time(self, user, day_delta=0, month_delta=0):
        """
        Retrieves flown hours of last 30 days. Accumulated
        :return: Integer Time
        """
        accumulated_time = 0
        # Construct the starting date to be considered

        start_date = datetime.today()

        if month_delta:
            start_date = self.add_months(start_date, -month_delta)

        start_date = start_date + timedelta(days=-day_delta)

        for flight in Flight.objects.filter(user=user). \
                order_by('flightleg__time_out'). \
                filter(flightleg__time_out__gte=start_date):
            hours = round(float(flight.flight_service_time.seconds) / 3600, 2)
            accumulated_time += hours

        return accumulated_time

    def get_current_month(self, user):
        """
        Retrieves flown hours of current month. Accumulated
        :return: Integer Time.
        """
        current_year = datetime.today().year
        current_month = datetime.today().month

        accumulated_time = 0

        for flight in Flight.objects.filter(user=user). \
                order_by('flightleg__time_out'). \
                filter(flightleg__time_out__year=current_year,
                       flightleg__time_out__month=current_month):
            hours = round(float(flight.flight_time.seconds) / 3600, 2)
            accumulated_time += hours

        return accumulated_time

    def get_last_calendar_year(self, user):
        """
        Retrieves flown hours of last calendar year. Accumulated
        :return: Integer Time.
        """
        target_year = datetime.today().year - 1

        accumulated_time = 0

        for flight in Flight.objects.filter(user=user). \
                order_by('flightleg__time_out'). \
                filter(flightleg__time_out__year=target_year):
            hours = round(float(flight.flight_time.seconds) / 3600, 2)
            accumulated_time += hours

        return accumulated_time

    def get_current_calendar_year(self, user):
        """
        Retrieves flown hours of last calendar year. Accumulated
        :return: Integer Time.
        """
        target_year = datetime.today().year
        accumulated_time = 0

        for flight in Flight.objects.filter(user=user). \
                order_by('flightleg__time_out'). \
                filter(flightleg__time_out__year=target_year):
            hours = round(float(flight.flight_time.seconds) / 3600, 2)
            accumulated_time += hours

        return accumulated_time

    def get_total_by_type(self, user, type_icao, day_delta=0):
        accumulated_time = 0

        start_date = self.add_months(datetime.today(), -day_delta)

        for flight in Flight.objects.filter(user=user). \
                order_by('flightleg__time_out'). \
                filter(flightleg__time_out__gte=start_date,
                       aircraft__model__short_name=type_icao):
            hours = round(float(flight.flight_time.seconds) / 3600, 2)
            accumulated_time += hours

        return accumulated_time


class CurrencyAsideMixin(ContextMixin):
    def get_currencies(self):
        currencies = []
        user = get_user(self.request)
        calc = CurrencyCalculator()

        def get_classes(accumulated, limit):
            pj = (accumulated * 100) / limit

            if pj < 50:
                return "currency-ok"
            elif pj < 70:
                return "currency-warning"
            elif pj < 100:
                return "currency-attention"
            else:
                return "currency-violation"

        # TOTAL HOURS
        accum = calc.get_all_time_data(user)
        limit = -1
        currencies.append({
            "code": "total_hours",
            "name": "Total",
            "value": accum,
            "limit": limit,
            "class": get_classes(accum, limit),
            "tooltip": "All time flown hours"
        })

        # TOTAL LAST 30 DAYS
        accum = calc.get_flight_last_x_time(day_delta=30, user=user)
        limit = self.request.user.settings.max_on_30
        currencies.append({
            "code": "total_last30",
            "name": "30 days",
            "value": accum,
            "limit": limit,
            "class": get_classes(accum, limit),
            "tooltip": "Hours flown in last 30 days"
        })

        # TOTAL LAST 90 DAYS
        accum = calc.get_flight_last_x_time(day_delta=90, user=user)
        limit = self.request.user.settings.max_on_90
        currencies.append({
            "code": "total_last90",
            "name": "90 days",
            "value": accum,
            "limit": limit,
            "class": get_classes(accum, limit),
            "tooltip": "Hours flown in last 90 days"
        })

        # TOTAL LAST 6 MONTHS
        accum = calc.get_flight_last_x_time(month_delta=6, user=user)
        limit = self.request.user.settings.max_on_6m
        currencies.append({
            "code": "total_last_6m",
            "name": "6 Months",
            "value": accum,
            "limit": limit,
            "class": get_classes(accum, limit),
            "tooltip": "Hours flown in last 6 months"
        })

        # TOTAL LAST 12 MONTHS
        accum = calc.get_flight_last_x_time(month_delta=12, user=user)
        limit = self.request.user.settings.max_on_12m
        currencies.append({
            "code": "total_last_12m",
            "name": "12 Months",
            "value": accum,
            "limit": limit,
            "class": get_classes(accum, limit),
            "tooltip": "Hours flown in last 12 months"
        })

        # TOTAL SERVICE TIME 30 DAYS
        accum = calc.get_service_last_x_time(user=user, day_delta=30)
        limit = self.request.user.settings.max_service_1m
        currencies.append({
            "code": "total_service_30d",
            "name": "Service 30 Days",
            "value": accum,
            "limit": limit,
            "class": get_classes(accum, limit),
            "tooltip": "Service time in last 30 days"

        })

        # TOTAL SERVICE TIME 90 DAYS
        accum = calc.get_service_last_x_time(user=user, day_delta=90)
        limit = self.request.user.settings.max_service_3m
        currencies.append({
            "code": "total_service_90d",
            "name": "Service 90 Days",
            "value": accum,
            "limit": limit,
            "class": get_classes(accum, limit),
            "tooltip": "Service time in last 90 days"
        })

        # TOTAL BY TYPE
        accum = calc.get_all_time_data(user)
        limit = -1
        currencies.append({
            "code": "total_b763",
            "name": "B763",
            "value": accum,
            "limit": limit,
            "class": get_classes(accum, limit),
            "tooltip": "Total hours flown in type"

        })

        # TOTAL VFR
        # TOTAL IFR

        return currencies

    def get_context_data(self, **kwargs):
        context = super(CurrencyAsideMixin, self).get_context_data(**kwargs)
        context['currencies'] = self.get_currencies()
        return context