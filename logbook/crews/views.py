from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from core.views import CurrencyAsideMixin
from crews.models import CrewMember


class ProcessCrewInsert(CreateView, CurrencyAsideMixin):
    template_name = 'crews/crewmember_insert.html'
    success_url = reverse_lazy('crews:manage')
    model = CrewMember
    # fields = ['reg_number', 'model', 'markings']


class ProcessCrewDelete(DeleteView, CurrencyAsideMixin):
    success_url = reverse_lazy('crews:manage')
    model = CrewMember


class ProcessCrewUpdate(UpdateView, CurrencyAsideMixin):
    model = CrewMember
    # fields = ['reg_number', 'model', 'markings']
    template_name_suffix = '_update'
    success_url = reverse_lazy('crews:manage')


class ProcessCrewManagement(ListView, CurrencyAsideMixin):
    model = CrewMember