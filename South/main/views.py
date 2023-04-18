from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

from main.models import Services, Rates, Rooms, Filials, Workers, Clients, Bookings



class MainView(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



class ListServices(ListView):
    template_name = 'main/list_model.html'
    model = Services
    context_object_name = 'model'


class ListRates(ListView):
    template_name = 'main/list_model.html'
    model = Rates
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_columns'] = 4
        return context  


class ListRooms(ListView):
    template_name = 'main/list_model.html'
    model = Rooms
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_columns'] = 5
        return context  


class ListFilials(ListView):
    template_name = 'main/list_model.html'
    model = Filials
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_columns'] = 5
        return context  


class ListWorkers(ListView):
    template_name = 'main/list_model.html'
    model = Workers
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_columns'] = 6
        return context  


class ListClients(ListView):
    template_name = 'main/list_model.html'
    model = Clients
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_columns'] = 6
        return context  


class ListBookings(ListView):
    template_name = 'main/list_model.html'
    model = Bookings
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_columns'] = 7
        return context  
