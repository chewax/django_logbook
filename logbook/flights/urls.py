from django.conf.urls import patterns, url
from flights.views import ProcessFlightView


urlpatterns = patterns('',

    url(r'^new', ProcessFlightView.as_view(), name='new'),

)

