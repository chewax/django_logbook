from django.contrib.auth.models import AnonymousUser
from django.db import models
from datetime import timedelta

from accounts.models import User
from aircrafts.models import Aircraft

# Create your models here.

class Flight(models.Model):
    user = models.ForeignKey(User, null=True)
    number = models.CharField(max_length=10, blank=True)
    aircraft = models.ForeignKey(Aircraft)

    def __unicode__(self):
        return '{}'.format(self.number)

    @property
    def flight_time(self):
        """
        Calculates the "flight time" of the flight,
        leaving out the block times.
        :return: timedelta: flight_time
        """
        flight_time = timedelta()
        for leg in self.flightleg_set.all():
            assert isinstance(leg, FlightLeg)
            flight_time += leg.time_on - leg.time_off

        return flight_time

    @property
    def block_time(self):
        """
        Calculates the "block time" of the flight.
        :return: timedelta: block_time
        """
        block_time = timedelta()
        for leg in self.flightleg_set.all():
            assert isinstance(leg, FlightLeg)
            block_time += leg.time_in - leg.time_out

        return block_time

    @property
    def flight_service_time(self):
        """
        Calculates the "service time" of the full flight.
        The time before and after the flight that conforms the
        total service time is not considered here.
        :return: timedelta: service_time
        """
        first_leg = self.flightleg_set.first()
        last_leg = self.flightleg_set.last()

        assert isinstance(first_leg, FlightLeg)
        assert isinstance(last_leg, FlightLeg)

        return last_leg.time_in - first_leg.time_out

    @property
    def departure_ICAO(self):
        legs = self.flightleg_set.first()
        return legs.departure_airport

    @property
    def arrival_ICAO(self):
        legs = self.flightleg_set.last()
        return legs.arrival_airport

    @property
    def date(self):
        legs = self.flightleg_set.first()
        return legs.time_out.date()

    @property
    def takeoffs(self):
        to_count = 0
        for leg in self.flightleg_set:
            to_count += leg.take_offs
        return to_count

    @property
    def landings(self):
        ldg_count = 0
        for leg in self.flightleg_set:
            ldg_count += leg.landings
        return ldg_count

class FlightLeg(models.Model):
    flight = models.ForeignKey(Flight)
    departure_airport = models.CharField(max_length=4, verbose_name="From:")
    arrival_airport = models.CharField(max_length=4, verbose_name="To:")
    take_offs = models.IntegerField(verbose_name="Takeoffs:", default=1)
    landings = models.IntegerField(verbose_name="Landings:", default=1)
    time_out = models.DateTimeField('OUT')
    time_off = models.DateTimeField('OFF')
    time_on = models.DateTimeField('ON')
    time_in = models.DateTimeField('IN')

    def __unicode__(self):
        return '{} :: {} - {}'.format(self.flight.number, self.departure_airport, self.arrival_airport)