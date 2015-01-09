from django.conf.urls import patterns, url
from flights.views import ProcessFlightView, ProcessFlightDeletion, \
    ProcessFlightUpdate


urlpatterns = patterns('',

    url(r'^new', ProcessFlightView.as_view(), name='new'),
    url(r'^delete/(?P<pk>\d+)', ProcessFlightDeletion.as_view(), name='delete'),
    url(r'^update/(?P<pk>\d+)', ProcessFlightUpdate.as_view(), name='update'),

)

