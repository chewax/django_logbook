from django.forms import ModelForm

from user_settings.models import UserSettings


class SettingsEntryForm(ModelForm):
    class Meta:
            model = UserSettings
            exclude = ['user', 'name']