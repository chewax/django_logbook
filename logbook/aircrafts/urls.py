from django.conf.urls import patterns, url
from aircrafts.views import ProcessAircraftInsert, ProcessAircraftManagement,\
    ProcessAircraftUpdate, ProcessAircraftDelete


urlpatterns = patterns('',

    url(r'^update/(?P<pk>\d+)', ProcessAircraftUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)', ProcessAircraftDelete.as_view(), name='delete'),
    url(r'^new', ProcessAircraftInsert.as_view(), name='new'),
    url(r'^manage', ProcessAircraftManagement.as_view(), name='manage'),

)

