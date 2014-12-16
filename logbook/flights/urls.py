from django.conf.urls import patterns, url
from flights.views import ProcessFlightView


urlpatterns = patterns('',

    url(r'^$', ProcessFlightView.as_view(), name='add_flight'),

)

