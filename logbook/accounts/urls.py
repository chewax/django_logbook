from django.conf.urls import patterns, url
from accounts.views import RegisterUserView


urlpatterns = patterns('',

    url(r'^register', RegisterUserView.as_view(), name='user_profile'),

)
