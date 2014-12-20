from django.conf.urls import patterns, url
from dashboard.views import DashboardProcessView


urlpatterns = patterns('',

    url(r'^', DashboardProcessView.as_view(), name='user_dashboard'),

)

