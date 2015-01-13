from django.conf.urls import patterns, url
from user_settings.views import ProcessSettingsView


urlpatterns = patterns('',

    url(r'^update/(?P<pk>\d+)', ProcessSettingsView.as_view(), name='user_settings'),

)

