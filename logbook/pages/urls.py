from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from accounts.views import LoginUserView
from pages.views import HomeView


urlpatterns = patterns('',
    url(r'^logout$', logout, {'next_page': 'pages:home'}, name='logout'),
    url(r'^login$', LoginUserView.as_view(), name='logout'),
    url(r'^', HomeView.as_view(), name='home'),
)
