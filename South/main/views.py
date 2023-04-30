from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

from main.models import Services, Rates, Rooms, Filials, Workers, Clients, Bookings, LocalSqlQueries

from django.db.models.fields import Field


class OccupancyRate(View):

    def get(self, request, *args, **kwargs):
        local_tuple = LocalSqlQueries.occupancy_rate()
        print(local_tuple)
        return JsonResponse(result)


class Birthday(View):
    
    def get(self, request, *args, **kwargs):
        return JsonResponse(result)


class PopularFilialType(View):
    
    def get(self, request, *args, **kwargs):
        return JsonResponse(result)


class PopularTypeRooms(View):
    
    def get(self, request, *args, **kwargs):
        return JsonResponse(result)


class PopularRates(View):
    
    def get(self, request, *args, **kwargs):
        return JsonResponse(result)


class UnpopularFilial(View):
    
    def get(self, request, *args, **kwargs):
        return JsonResponse(result)



class MainView(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



class ListServices(ListView):
    template_name = 'main/list/list_services.html'
    model = Services
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['service_id', 'title', 'description', 'price']
        context['name_fields'] = name_fields
        return context  


class ListRates(ListView):
    template_name = 'main/list/list_rates.html'
    model = Rates
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['rate_id', 'title', 'description', 'price']
        context['name_fields'] = name_fields
        return context  


class ListRooms(ListView):
    template_name = 'main/list/list_rooms.html'
    model = Rooms
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['room_id', 'number', 'type_number', 'busy', 'client']
        context['name_fields'] = name_fields
        return context  


class ListFilials(ListView):
    template_name = 'main/list/list_filials.html'
    model = Filials
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['filial_id', 'title', 'address', 'phone', 'email']
        context['name_fields'] = name_fields
        return context  


class ListWorkers(ListView):
    template_name = 'main/list/list_workers.html'
    model = Workers
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['worker_id', 'name', 'post', 'phone', 'email', 'address']
        context['name_fields'] = name_fields
        return context   


class ListClients(ListView):
    template_name = 'main/list/list_clients.html'
    model = Clients
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['client_id', 'name', 'birthday', 'gender', 'phone', 'email']
        context['name_fields'] = name_fields
        return context  


class ListBookings(ListView):
    template_name = 'main/list/list_bookings.html'
    model = Bookings
    context_object_name = 'models'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.get_fields()
        name_fields = ['booking', 'client', 'filial', 'arrival_date', 'departue_date', 'room', 'rate']
        context['name_fields'] = name_fields
        return context   
