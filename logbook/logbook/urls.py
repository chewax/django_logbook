from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^flights/', include('flights.urls', namespace='flights')),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^settings/', include('user_settings.urls', namespace='settings')),
    url(r'', include('social_auth.urls')),
    url(r'^', include('pages.urls', namespace='pages')),

)
