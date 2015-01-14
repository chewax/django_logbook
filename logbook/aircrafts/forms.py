from django.forms import ModelForm
from aircrafts.models import Aircraft

class AircraftForm(ModelForm):
    class Meta:
            model = Aircraft
            exclude = ['user']
