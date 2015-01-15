from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from core.views import CurrencyAsideMixin
from aircrafts.models import Aircraft, AircraftType


class ProcessAircraftInsert(CreateView, CurrencyAsideMixin):
    template_name = 'aircrafts/aircraft_insert.html'
    success_url = reverse_lazy('aircrafts:manage')
    model = Aircraft
    fields = ['reg_number', 'model', 'markings']


class ProcessAircraftDelete(DeleteView, CurrencyAsideMixin):
    success_url = reverse_lazy('aircrafts:manage')
    model = Aircraft


class ProcessAircraftUpdate(UpdateView, CurrencyAsideMixin):
    model = Aircraft
    fields = ['reg_number', 'model', 'markings']
    template_name_suffix = '_update'
    success_url = reverse_lazy('aircrafts:manage')


class ProcessAircraftManagement(ListView, CurrencyAsideMixin):
    model = Aircraft