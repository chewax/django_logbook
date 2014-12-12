from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin$', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^logout$', logout, {'next_page': 'login'}, name='logout'),
    # url(r'^login$', login, {'template_name': 'accounts/login.html'}, name='login'),
    # url(r'^', include('pages.urls', namespace='pages')),
    url(r'^', login, {'template_name': 'accounts/login.html'}, name='login'),
)
