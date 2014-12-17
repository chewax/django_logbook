from django.db import models

from datetime import timedelta
# Create your models here.

class Flight(models.Model):
    number = models.CharField(max_length=10, blank=True)
    flight_origin_ICAO = models.CharField(max_length=4, blank=True, null=True, verbose_name="From")
    flight_dest_ICAO = models.CharField(max_length=4, blank=True, null=True, verbose_name="To")

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

class FlightLeg(models.Model):
    flight = models.ForeignKey(Flight)
    departure_airport = models.CharField(max_length=4)
    arrival_airport = models.CharField(max_length=4)
    time_out = models.DateTimeField('Time OUT')
    time_off = models.DateTimeField('Time OFF')
    time_on = models.DateTimeField('Time ON')
    time_in = models.DateTimeField('Time IN')

    def __unicode__(self):
        return '{} :: {} - {}'.format(self.flight.number, self.departure_airport, self.arrival_airport)