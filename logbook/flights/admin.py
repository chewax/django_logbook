from django.contrib import admin
from flights.models import Flight, FlightLeg

# Register your models here.


class FlighLegInline(admin.TabularInline):
    model = FlightLeg
    extra = 3

class FlightAdmin(admin.ModelAdmin):
    inlines = [FlighLegInline]
    list_display = ['number', 'get_flight_time']

admin.site.register(Flight, FlightAdmin)
