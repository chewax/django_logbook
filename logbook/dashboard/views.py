from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from flights.models import Flight


class DashboardProcessView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    # model = Flight

    def get_context_data(self, **kwargs):
        context = super(DashboardProcessView, self).get_context_data(**kwargs)
        append_context = []
        user = self.request.user
        if self.request.method == 'POST':
            input_query = self.request.POST["query_input"]
            print('input_query = {}'.format(input_query))

            if input_query:
                q = Q(aircraft__reg_number__contains=input_query) \
                    | Q(aircraft__model__short_name__contains=input_query) \
                    | Q(number__contains=input_query) \
                    | Q(flightleg__departure_airport__contains=input_query) \
                    | Q(flightleg__arrival_airport__contains=input_query)

                q = q & Q(user=user)

                #TODO Add Distinct to this query -- .distinct('pk')
                #Now it is not supported by the database backend
                context['flights'] = Flight.objects.filter(q)
            else:
                context['flights'] = Flight.objects.filter(user=user)
        else:
            context['flights'] = Flight.objects.filter(user=user)

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, **kwargs)
