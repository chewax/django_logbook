from django.views.generic import UpdateView
from core.views import CurrencyAsideMixin
from user_settings.forms import SettingsEntryForm
from user_settings.models import UserSettings


class ProcessSettingsView(UpdateView, CurrencyAsideMixin):
    form_class = SettingsEntryForm
    template_name = 'user_settings/settings_base.html'
    success_url = '/dashboard/'
    model = UserSettings