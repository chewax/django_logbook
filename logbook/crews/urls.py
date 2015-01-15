from django.conf.urls import patterns, url
from crews.views import ProcessCrewInsert, ProcessCrewManagement,\
    ProcessCrewDelete, ProcessCrewUpdate


urlpatterns = patterns('',

    url(r'^update/(?P<pk>\d+)', ProcessCrewUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)', ProcessCrewDelete.as_view(), name='delete'),
    url(r'^new', ProcessCrewInsert.as_view(), name='new'),
    url(r'^manage', ProcessCrewManagement.as_view(), name='manage'),

)

