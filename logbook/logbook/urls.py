from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^flights/', include('flights.urls', namespace='flights')),
    url(r'^', include('pages.urls', namespace='pages')),

)
