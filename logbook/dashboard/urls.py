from django.conf.urls import patterns, url
from dashboard.views import DashboardProcessView, FlightData


urlpatterns = patterns('',

    url(r'^get_flight_data', FlightData.as_view(), name='user_dashboard'),
    url(r'^', DashboardProcessView.as_view(), name='user_dashboard'),

)

