from django.shortcuts import redirect
from django.views.generic import UpdateView
from core.views import CurrencyAsideMixin
from user_settings.forms import SettingsEntryForm
from user_settings.models import UserSettings


class ProcessSettingsView(UpdateView, CurrencyAsideMixin):
    form_class = SettingsEntryForm
    template_name = 'user_settings/settings_base.html'
    success_url = '/dashboard/'
    model = UserSettings

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.settings.pk == int(kwargs['pk']):
            return super(ProcessSettingsView, self).get(request, *args, **kwargs)
        else:
            return redirect('/settings/update/{}'.format(user.settings.pk))