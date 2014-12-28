from django.contrib import admin

from aircrafts.models import AircraftType, Aircraft

# class AicraftAdmin(admin.TabularInline):
#     model = Aircraft
#     extra = 3
#
# class AircraftModelAdmin(admin.ModelAdmin):
#     list_display = ['factory', 'original_release', 'update_number', 'short_name', 'description']

admin.site.register(AircraftType)
admin.site.register(Aircraft)